# tests/test_urls.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.View.user_view import UserSignUpAPIView

class TestUserURLs(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse('user-register')
        resolved_view = resolve(url)
        self.assertEqual(resolved_view.func.view_class, UserSignUpAPIView)
