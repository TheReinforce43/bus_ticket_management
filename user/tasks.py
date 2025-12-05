from celery import shared_task 
from django.contrib.auth import get_user_model 
from support_function.email_helpers import UserSignUpEmail

import logging 

User = get_user_model() 
logger = logging.getLogger(__name__)

@shared_task()
def test_task():
    return "This is a test task from Celery!"


@shared_task

def daily_summary_task():
    logger.info("Daily summary task executed.")
    # Here you can add the logic for your daily summary email
    return "Daily summary task completed."


@shared_task(bind=True,max_retries=5,default_retry_delay=10)
def send_welcome_email(self,user_id):

    try:

        user= User.objects.get(id=user_id)
        UserSignUpEmail().send_signup_email(user)
        logger.info(f"Welcome email sent to user id {user_id}")
    
    except User.DoesNotExist as e:
        logger.error(f"failed to send mail to : {user.email} {e}")
        raise self.retry(exc=e,countdown=10)