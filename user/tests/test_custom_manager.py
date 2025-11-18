from django.test import TestCase 
from user.models import User 



class CustomUserManagerTest(TestCase):

    def test_create_user(self):
        user_instance = User.objects.create(
            email='mahi@gmail.com',
            password='1234'
        )

        self.assertEqual(user_instance.email,"mahi@gmail.com")
        self.assertEqual(user_instance.password,"1234")
        self.assertEqual(user_instance.role,"Passenger")

        