from django.test import TestCase
from .forms import BugForm, CommentForm

class Bug_Create_Test(TestCase):
    def test_can_create_Bug(self):
        form = BugForm({"name":"test", "description": "Test"})
        self.assertTrue(form.is_valid())
    def test_cant_have_name_as_empty_string(self):
        form = BugForm({"name":"", "description": "Test"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
    def test_cant_have_description_as_empty_string(self):
        form = BugForm({"name":"test", "description": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])

class Comment_Forms(TestCase):
    def can_make_comment(self):
        form = CommentForm({"content": "1"})
        self.assertTrue(form.is_valid())
    def cant_have_content_be_empty_string(self):
        form = CommentForm({"content": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])