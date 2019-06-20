from django.test import TestCase
from .models import Bug

class TestViews(TestCase):
    
    def test_get_Bug_page(self):
        page = self.client.get("/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")
        
    def get_Bug_detail_page(self):
      bug = Bug({"name":"test", "description":"description"})
      bug.save()
      page = self.client.get("/bug/{0}".format(bug.id))
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, "bugdetail.html")
        
    def test_get_page_for_bug_that_does_not_exist(self):
        page = self.client.get("/bug/10")
        self.assertEqual(page.status_code, 404)
        
    def create_bug_page(self):
        page = self.client.get("/bug/new")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'bugform.html')