from django import template

from templatetag_sugar.register import tag
from templatetag_sugar.parser import Name, Variable, Constant, Optional, Model

register = template.Library()


@tag(register, [Constant("for"), Variable(), Optional([Constant("as"), Name()])])
def test_tag_1(context, val, asvar=None):
    if asvar:
        context[asvar] = val
        return ""
    else:
        return val

@tag(register, [Model(), Variable(), Optional([Constant("as"), Name()])])
def test_tag_2(context, model, limit, asvar=None):
    objs = model._default_manager.all()[:limit]
    if asvar:
        context[asvar] = objs
        return ""
    return unicode(objs)
