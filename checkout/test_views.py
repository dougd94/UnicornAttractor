from django.test import TestCase


class Checkout_test(TestCase):
    
    def test_get_checkout_page(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 302)
        
 