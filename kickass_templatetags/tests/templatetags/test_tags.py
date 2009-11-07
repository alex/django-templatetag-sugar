from django import template

from kickass_templatetags.register import tag
from kickass_templatetags.parser import Name, Variable, Constant, Optional

register = template.Library()


@tag(register, [Constant("for"), Variable(), Optional([Constant("as"), Name()])])
def test_tag_1(context, args, kwargs):
    val = args[0]
    if len(args) == 2:
        context[args[1]] = val
        return ""
    else:
        return val
