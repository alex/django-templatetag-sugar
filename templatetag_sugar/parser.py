from collections import deque
from copy import copy

from django.db.models.loading import cache
from django.template import TemplateSyntaxError

from templatetag_sugar.node import SugarNode


class Parser(object):
    def __init__(self, syntax, function):
        self.syntax = syntax
        self.function = function
    
    def __call__(self, parser, token):
        # we're going to be doing pop(0) a bit, so a deque is way more 
        # efficient
        bits = deque(token.split_contents())
        # pop the name of the tag off
        tag_name = bits.popleft()
        pieces = []
        error = False
        for part in self.syntax:
            try:
                result = part.parse(parser, bits)
            except TemplateSyntaxError:
                error = True
                break
            if result is None:
                continue
            pieces.extend(result)
        if bits or error:
            raise TemplateSyntaxError("%s has the following syntax: {%% %s %s %%}" % (
                tag_name,
                tag_name,
                " ".join(part.syntax() for part in self.syntax),
            ))
        return SugarNode(pieces, self.function)


class Parsable(object):
    def resolve(self, context, value):
        return value

class NamedParsable(Parsable):
    def __init__(self, name=None):
        self.name = name
    
    def syntax(self):
        if self.name:
            return "<%s>" % self.name
        return "<arg>"

class Constant(Parsable):
    def __init__(self, text):
        self.text = text

    def syntax(self):
        return self.text
    
    def parse(self, parser, bits):
        if not bits:
            raise TemplateSyntaxError
        if bits[0] == self.text:
            bits.popleft()
            return None
        raise TemplateSyntaxError
    

class Variable(NamedParsable):
    def parse(self, parser, bits):
        bit = bits.popleft()
        val = parser.compile_filter(bit)
        return [(self, self.name, val)]
    
    def resolve(self, context, value):
        return value.resolve(context)

class Name(NamedParsable):
    def parse(self, parser, bits):
        bit = bits.popleft()
        return [(self, self.name, bit)]


class Optional(Parsable):
    def __init__(self, parts):
        self.parts = parts
    
    def syntax(self):
        return "[%s]" % (" ".join(part.syntax() for part in self.parts))
    
    def parse(self, parser, bits):
        result = []
        # we make a copy so that if part way through the optional part it
        # doesn't match no changes are made
        bits_copy = copy(bits)
        for part in self.parts:
            try:
                val = part.parse(parser, bits_copy)
                if val is None:
                    continue
                result.extend(val)
            except (TemplateSyntaxError, IndexError):
                return None
        # however many bits we popped off our copy pop off the real one
        diff = len(bits) - len(bits_copy)
        for _ in xrange(diff):
            bits.popleft()
        return result


class Model(NamedParsable):
    def parse(self, parser, bits):
        bit = bits.popleft()
        app, model = bit.split(".")
        return [(self, self.name, cache.get_model(app, model))]
