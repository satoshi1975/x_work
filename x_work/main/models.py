from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    '''Main user model'''
    username=models.CharField(unique=False)
    email = models.EmailField(unique=True)
    user_type=models.CharField(max_length=20)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Cities(models.Model):
    '''City model'''
    id=models.BigAutoField(primary_key=True,default=None)
    city = models.CharField(blank=True, null=True)
    state_name = models.CharField(blank=True, null=True)

    class Meta:
        db_table = 'cities'

class Occupation(models.Model):
    '''Occupation model'''
    occupation=models.CharField(max_length=100)
    
    def __str__(self):
        return self.occupation
        

class Articles(models.Model):
    '''Articles model'''
    title=models.CharField(max_length=500,default=None)
    text=models.TextField()

    def __str__(self):
        return self.title