from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from main.models import User
from employers.models import Employer
from job_seekers.models import JobSeeker
from django.contrib.gis.db import models

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20)
    # user_type=forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class UpdateEmployerForm(forms.ModelForm):
    
    class Meta:
        model = Employer
        fields = ('company_name', 'description', 'industry', 'phone_number','address','website',)

class UpdateJobseekerForm(forms.ModelForm):
    
    class Meta:
        model = JobSeeker
        fields = ('bio', 'skills', 'experience', 'education','desired_salary','address','phone_number','first_name','last_name')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)