from django.template import Template, Context, TemplateSyntaxError
from django.test import TestCase

from templatetag_sugar.tests.models import Book


class SugarTestCase(TestCase):
    def assert_renders(self, tmpl, context, value):
        tmpl = Template(tmpl)
        self.assertEqual(tmpl.render(context), value)
    
    def assert_syntax_error(self, tmpl, error):
        try:
            Template(tmpl)
        except TemplateSyntaxError, e:
            self.assertTrue(
                str(e).endswith(error),
                "%s didn't end with %s" % (str(e), error)
            )
        else:
            self.fail("Didn't raise")
    
    
    def test_basic(self):
        self.assert_renders(
            """{% load test_tags %}{% test_tag_1 for "alex" %}""",
            Context(),
            "alex"
        )
        
        c = Context()
        self.assert_renders(
            """{% load test_tags %}{% test_tag_1 for "brian" as name %}""",
            c,
            ""
        )
        self.assertEqual(c["name"], "brian")
        
        
        self.assert_renders(
            """{% load test_tags %}{% test_tag_1 for variable %}""",
            Context({"variable": [1, 2, 3]}),
            "[1, 2, 3]",
        )
        
    def test_model(self):
        Book.objects.create(title="Pro Django")
        self.assert_renders(
            """{% load test_tags %}{% test_tag_2 tests.Book 2 %}""",
            Context(),
            "[<Book: Pro Django>]"
        )
    
    def test_errors(self):
        self.assert_syntax_error(
            """{% load test_tags %}{% test_tag_1 for "jesse" as %}""",
            "test_tag_1 has the following syntax: {% test_tag_1 for <arg> [as <arg>] %}"
        )
        
        self.assert_syntax_error(
            """{% load test_tags %}{% test_tag_4 width %}""",
            "test_tag_4 has the following syntax: {% test_tag_4 [width <width>] [height <height>] %}"
        )

    def test_variable_as_string(self):
        self.assert_renders(
            """{% load test_tags %}{% test_tag_3 "xela alex" %}""",
            Context(),
            "xela alex",
        )

    def test_optional(self):
        self.assert_renders(
            """{% load test_tags %}{% test_tag_4 width 100 height 200 %}""",
            Context(),
            "100, 200",
        )
        
        self.assert_renders(
            """{% load test_tags %}{% test_tag_4 width 100 %}""",
            Context(),
            "100, None"
        )
        
        self.assert_renders(
            """{% load test_tags %}{% test_tag_4 height 100 %}""",
            Context(),
            "None, 100",
        )
        
        self.assert_syntax_error(
            """{% load test_tags %}{% test_tag_1 %}""",
            "test_tag_1 has the following syntax: {% test_tag_1 for <arg> [as <arg>] %}"
        )
