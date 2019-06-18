from django.test import TestCase
from .forms import UserRegistrationForm

class CanCreateAccount(TestCase):
    
    def test_can_create_account(self):
        form = UserRegistrationForm({'username':"TestUser", "password1": "123456qw", "password2": "123456qw", "email": "123@gmail.com"})
        self.assertTrue(form.is_valid())
        
    def cant_create_account_with_non_matching_password(self):
        form = UserRegistrationForm({'username':"TestUser", "password1": "123456", "password2": "123456qw", "email": "123@gmail.com"})
        self.assertFalse(form.is_valid())
        
    def cant_create_account_without_a_username(self):
        form = UserRegistrationForm({"password1": "123456qw", "password2": "123456qw", "email": "123@gmail.com"})
        self.assertFalse(form.is_valid())
        
    def cant_pass_empty_string_as_username(self):
        form = UserRegistrationForm({"username":"","password1": "123456qw", "password2": "123456qw", "email": "123@gmail.com"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    