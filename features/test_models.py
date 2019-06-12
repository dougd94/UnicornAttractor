from django.test import TestCase
from .models import Feature
from django.contrib.auth.models import User


class TestFeatureModel(TestCase):
    # tests that auto paid = False
    def test_paid_defaults_to_False(self):
        user=User(username="test", password="test")
        user.save()
        feature = Feature(name="Create a Test", author=user)
        feature.save()
        self.assertEqual(feature.name, "Create a Test")
        self.assertFalse(feature.paid)
    def upvotes_are_1(self):
        # test that has one upvote on creation
        user=User(username="test", password="test")
        user.save()
        feature = Feature(name="Create a Test", author=user)
        feature.save()
        self.assertEqual(feature.name, "Create a Test")
        self.assertEqual(feature.upvotes, 1)