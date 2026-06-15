from django.test import TestCase 
from django.contrib.auth import get_user_model 
from unittest.mock import patch, MagicMock

from rest_framework_simplejwt.tokens import RefreshToken


from user.Serializer.user_serializer import(
    UserSignUpSerializer,
    UserLoginSerializer,
    UserLogoutSerializer,
    UserProfileSerializer
)

User  = get_user_model() 


class UserSignUpSerializerTest(TestCase):

    def _valid_payload(self,**overrides):

        payload = {
            "email":"farhan@gmail.com",
            "password":"pass123",
            "first_name":"Farhan",
            "last_name":"Ahmed",
            "role":"Passenger"
        }

        payload.update(overrides)
        return payload 

    def test_valid_payload_sign_up(self):

        serializer = UserSignUpSerializer(data = self._valid_payload()) 

        self.assertTrue(serializer.is_valid(),serializer.errors)


        user = serializer.save()

        self.assertEqual(user.email,"rahim@example.com")
        self.assertEqual(user.first_name,"Rahim")
        self.assertEqual(user.last_name,"Ahmed")
        self.assertEqual(user.role,"Passenger")
        self.assertTrue(user.check_password("pass123")) 
        



