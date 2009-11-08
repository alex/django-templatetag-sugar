from templatetag_sugar.parser import Parser


def tag(register, syntax, name=None):
    def inner(func):
        register.tag(name or func.__name__, Parser(syntax, func))
        return func
    return inner
