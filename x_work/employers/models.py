from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import User

class Employer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    email=models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    # user_permissions = models.ManyToManyField('auth.Permission', blank=True,related_name='employer')
    # groups = models.ManyToManyField('auth.Permission', blank=True, related_name='employer_set')


    def __str__(self):
        return self.company_name


