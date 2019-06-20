from django.test import TestCase
from .models import Feature

class TestViews(TestCase):
    def test_get_features_page(self):
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")
        
    def get_feature_detail_page(self):
      feature = Feature({"name":"test", "description":"description"})
      feature.save()
      page = self.client.get("/feature/{0}".format(feature.id))
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, "featuredetail.html")
        
    def test_get_page_for_feature_that_does_not_exist(self):
        page = self.client.get("/feature/10")
        self.assertEqual(page.status_code, 404)
        
    def create_feature_page(self):
        page = self.client.get("/feature/new")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'featureform.html')