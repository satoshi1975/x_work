from django.db import models
from main.models import User


class JobSeeker(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    username=models.CharField(max_length=50,blank=True)
    first_name=models.CharField(max_length=50, blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    desired_salary = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email=models.EmailField(max_length=255,default=None)

    def __str__(self):
        return self.user
