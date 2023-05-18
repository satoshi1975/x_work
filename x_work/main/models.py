from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # CHOICES = (
    #     ('JS', 'job_seeker'),
    #     ('ER', 'employer'),
    # )
    username=models.CharField(unique=False)
    email = models.EmailField(unique=True)
    user_type=models.CharField(max_length=20)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []