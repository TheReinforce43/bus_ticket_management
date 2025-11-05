from django.db import models

from user.custom_manager import CustomUserManager
from django.contrib.auth.models import  AbstractUser 
from django.utils.translation import gettext_lazy as _  



class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True) 

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email