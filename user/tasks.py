from celery import shared_task 
from django.contrib.auth import get_user_model 
from support_function.email_helpers import UserSignUpEmail

User = get_user_model() 

@shared_task 
def test_task():
    return "This is a test task from Celery!"


@shared_task 
def send_welcome_email(user_id):

    user= User.objects.get(id=user_id)
    UserSignUpEmail().send_signup_email(user)
    