from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from main.models import User
from employers.models import Employer
from job_seekers.models import JobSeeker

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20)
    # user_type=forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class CreateEmployerForm(UserCreationForm):
    class Meta:
        model = Employer
        fields = ('email', 'company_name', 'phone_number')

class CreateJobseekerForm(UserCreationForm):
    class Meta:
        model = JobSeeker
        fields = ('email', 'first_name', 'last_name','phone_number')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)