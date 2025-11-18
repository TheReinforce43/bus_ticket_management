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

        serializer = UserProfileSerializer(data=user_instance)
        self.assertTrue(serializer.is_valid()) 
        self.assertEqual(serializer.data['email'],user_instance.email)
        user = serializer.save()

        self.assertIsInstance(user, User)
        self.assertEqual(user.check_password("testpassword"), True)

    def test_invalid_user_profile_serializer(self):
        invalid_data = {
            'email': 'invalidemail',
            'password': '',
        }

        serializer = UserProfileSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)
        self.assertIn('password', serializer.errors)