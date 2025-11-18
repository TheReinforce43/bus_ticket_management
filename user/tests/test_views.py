from rest_framework.test import APITestCase 

from django.urls import reverse 
from user.models import User 
from rest_framework import status 

class TestUserRegisterView(APITestCase):

    def test_user_registration(self):
        url = reverse("user-register")
        data = {"email": "newuser@example.com", "password": "pass123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="newuser@example.com").exists())
