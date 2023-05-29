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

class Cities(models.Model):
    id=models.BigAutoField(primary_key=True,default=None)
    city = models.CharField(blank=True, null=True)
    state_name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'

class Occupation(models.Model):
    # id=models.AutoField(primary_key=True)
    occupation=models.CharField(max_length=100)
    
    def __str__(self):
        return self.occupation
        