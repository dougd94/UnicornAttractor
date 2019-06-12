from django.test import TestCase


class TestViews(TestCase):

    def wrong_url_cart_page(self):
        page = self.client.get("/cart")
        self.assertEqual(page.status_code, 404)
        self.assertTemplateUsed(page, "134.html")