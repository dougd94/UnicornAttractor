from django.test import TestCase
from .models import Feature

class TestViews(TestCase):
    def test_get_features_page(self):
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")
        
   
        
    def test_get_edit_page_for_feature_that_does_not_exist(self):
        page = self.client.get("/feature/1")
        self.assertEqual(page.status_code, 404)