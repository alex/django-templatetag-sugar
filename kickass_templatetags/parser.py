from collections import deque

from django.template import TemplateSyntaxError


class Parser(object):
    def __init__(self, syntax, function):
        self.syntax = syntax
        self.function = function
    
    def __call__(self, parser, token):
        # we're going to be doing pop(0) a bit, so a deque is way more 
        # efficient
        bits = deque(token.split_contents())
        # pop the name of the tag off
        bits.popleft()
        pieces = []
        for part in self.syntax:
            result = part.parse(parser, bits)
            if result is None:
                continue
            pieces.append((part, result))
        if bits:
            raise TemplateSyntaxError("You didn't eat all the bits")
        return KickassNode(args, kwargs, self.function)


class Parsable(object):
    pass

class Constant(Parsable):
    def __init__(self, text):
        self.text = text
        super(Constant, self).__init__()
    
    def parse(self, parser, bits):
        if bits[0] == self.text:
            bits.popleft()
            return None
        raise TemplateSyntaxError("%s expected, %s found" % (self.text, bits[0]))


class Variable(Parsable):
    def __init__(self, name=None):
        self.name = name
    
    def parse(self, parser, bits):
        bit = bits.popleft()
        val = parser.compile_filter(bit)
        return (self.name, val)
    
    def resolve(self, context, value):
        return value.resolve(context)

class Name(Parsable):
    def __init__(self, name=None):
        self.name = name
    
    def parser(self, parser, bits):
        bit = bits.popleft()
        return (self.name, bit)
    
    def resolve(self, context, value):
        return value
