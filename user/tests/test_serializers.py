from django.test import TestCase 
from user.models import User 

from user.Serializer.user_serializer import UserProfileSerializer 


class TestUserProfileSerializer(TestCase):


    def test_valid_user_profile_serializer(self):
        user_instance = User.objects.create(
            email="test@gmail.com",
            password="testpassword",
            role="Passenger"
        )

        serializer = UserProfileSerializer(user_instance)
        # self.assertTrue(serializer.is_valid()) 
        # self.assertEqual(serializer.data['email'],user_instance.email)
        # user = serializer.save()


        self.assertEqual(serializer.data['email'], user_instance.email)
        self.assertEqual(serializer.data['role'], user_instance.role)

    def test_invalid_user_profile_serializer(self):
        invalid_data = {
            'email': 'invalidemilgmail.com',
            'password': '123',
        }

        serializer = UserProfileSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)
        self.assertIn('password', serializer.errors)