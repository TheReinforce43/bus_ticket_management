from django.core.mail import send_mail 
from  django.conf import settings 
from django.utils.html import strip_tags 
import logging 
from django.template.loader import render_to_string 

from django.core.mail import EmailMultiAlternatives


logger = logging.getLogger(__name__) 






class UserSignUpEmail:

    _instance = None 

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    

    def send_signup_email(self,user):

     
        html_content =render_to_string(

            'signup/signup_templates.html',
            {
                "user": user,
                "year": 2025
            }
        )

        text_content = strip_tags(html_content)

        print(f"html_content : {html_content}") 

        email = EmailMultiAlternatives(
            subject= 'Welcome to Bus Ticket Booking System',
            body= text_content,
            from_email= settings.DEFAULT_FROM_EMAIL,
            to= [user.email]

        )

        email.attach_alternative(html_content, "text/html")

        logger.info(f"Sending signup email to {user.email}")
        email.send()


    


        
