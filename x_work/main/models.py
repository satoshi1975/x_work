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

# class Geol(models.Model):
#     state_name=models.CharField(max_length=50)
#     city_name=models.CharField(max_length=50)
#     class Meta:
#         managed = True
#         # db_table = 'city'


class City(models.Model):
    city = models.CharField(blank=True, null=True)
    state_name = models.CharField(blank=True, null=True)

