from django.template import Template, Context
from django.test import TestCase

from kickass_templatetags.tests.models import Book


class KickassTestCase(TestCase):
    def test_basic(self):
        tmpl = Template("""{% load test_tags %}{% test_tag_1 for "alex" %}""")
        self.assertEqual(tmpl.render(Context()), "alex")
        
        tmpl = Template("""{% load test_tags %}{% test_tag_1 for "brian" as name %}""")
        context = Context()
        tmpl.render(context)
        self.assertEqual(context["name"], "brian")
        
        tmpl = Template("""{% load test_tags %}{% test_tag_1 for variable %}""")
        context = Context({"variable": [1, 2, 3]})
        self.assertEqual(tmpl.render(context), "[1, 2, 3]")
    
    def test_model(self):
        Book.objects.create(title="Pro Django")
        tmpl = Template("""{% load test_tags %}{% test_tag_2 tests.Book 2 %}""")
        self.assertEqual(tmpl.render(Context()), "[<Book: Pro Django>]")
