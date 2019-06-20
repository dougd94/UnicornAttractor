from django.test import TestCase
from .forms import OrderForm

class CanCreateAccount(TestCase):
    def test_can_enter_details(self):
        form = OrderForm({'full_name':"TestUser", "phone_number": "123456qw", "country": "123456qw", "town_or_city": "12333", "county":"10","street_address1":"10",
        "street_address2": "22", "postcode": "111" })
        self.assertTrue(form.is_valid())
    def test_cant_have_no_name(self):
        form = OrderForm({'full_name':"", "phone_number": "123456qw", "country": "123456qw", "town_or_city": "12333", "county":"10","street_address1":"10",
        "street_address2": "22", "postcode": "111" })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])

