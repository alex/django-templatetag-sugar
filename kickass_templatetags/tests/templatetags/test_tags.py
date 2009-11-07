from django import template

from kickass_templatetags.register import tag
from kickass_templatetags.parser import Name, Variable, Constant, Optional

register = template.Library()


@tag(register, [Constant("for"), Variable(), Optional([Constant("as"), Name()])])
def test_tag_1(context, val, asvar=None):
    if asvar:
        context[asvar] = val
        return ""
    else:
        return val
