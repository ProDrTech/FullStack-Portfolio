from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_images/', default='profile_images/default.webp')
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)