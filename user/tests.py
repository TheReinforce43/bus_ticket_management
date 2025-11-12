from django.test import TestCase , SimpleTestCase 
from django.urls import reverse, resolve  


class TestUserUrls(SimpleTestCase): 

    def test_user_app_url_is_resolved(self):
        url = reverse('user-signup')

        print(f"Resolved  Sign Up URL: {url}")  # Debugging line to print the resolved URL

        self.assertEqual(resolve(url).func.view_class.__name__, 'UserSignUpAPIView')

    def test_user_login_url_is_resolved(self):
        url = reverse('user-login')
        print(f"Resolved Login URL: {url}")  # Debugging line to print the resolved URL

        self.assertEqual(resolve(url).func.view_class.__name__, 'UserLoginAPIView')

    def test_user_logout_url_is_resolved(self):
        url = reverse('user-logout')
        print(f"Resolved Logout URL: {url}")  # Debugging line to print the resolved URL
        self.assertEqual(resolve(url).func.view_class.__name__, 'UserLogoutAPIView')

