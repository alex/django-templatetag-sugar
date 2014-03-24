django-templatetag-sugar
===========================

A library to make writing templatetags in Django sweet.

Here's an example of using:

.. code-block:: python

    from django import template

    from templatetag_sugar.register import tag
    from templatetag_sugar.parser import Name, Variable, Constant, Optional, Model

    register = template.Library()

    @tag(register, [Constant("for"), Variable(), Optional([Constant("as"), Name()])]):
    def example_tag(context, val, asvar=None):
        if asvar:
            context[asvar] = val
            return ""
        else:
            return val


As you can see it makes it super simple to define the syntax for a tag.
