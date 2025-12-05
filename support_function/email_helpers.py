from django.core.mail import send_mail 
from  django.conf import settings 


class UserSignUpEmail:

    _instance = None 

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    

    def send_signup_email(self,user):

        subject = 'Welcome to Bus Ticket Booking System'
        message = f'Hi {user.first_name}, thank you for signing up for our Bus Ticket Booking System. We are excited to have you on board!'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]

        send_mail(
            subject, 
            message, 
            from_email, 
            recipient_list,
            fail_silently=False
            )

