from django.test import TestCase
from .forms import UserRegistrationForm

class CanCreateAccount(TestCase):
    def test_can_create_account(self):
        form = UserRegistrationForm({'username':"TestUser", "password1": "123456qw", "password2": "123456qw", "email": "123@gmail.com"})
        self.assertTrue(form.is_valid())

    