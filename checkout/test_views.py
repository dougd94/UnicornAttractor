from django.test import TestCase


class Checkout_test(TestCase):
    
    def test_get_checkout_page(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
        
    def test_get_checkout_page_if_wrong_url(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 404)
        self.assertTemplateUsed(page, "checkout22.html")