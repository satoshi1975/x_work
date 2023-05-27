import os
from uuid import uuid4
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from main.models import User, Cities
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



class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class ProfilePhotoMixin:
    def generate_filename(self, filename):
        extension = filename.split('.')[-1]  # получаем расширение файла
        filename = f'{uuid4().hex}.{extension}'  # генерируем новое имя файла
        return filename

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        profile_photo = self.files.get('profile_photo')
        print(profile_photo)
        # print(type(profile_photo))
        if profile_photo:
            print('yes')
            old_profile_photo = self.instance.profile_photo
            if old_profile_photo:
                old_profile_photo.delete()

            profile_photo.name = self.generate_filename(profile_photo.name)
            cleaned_data['profile_photo'] = profile_photo
            return cleaned_data
        else:pass
class UpdateEmployerForm(ProfilePhotoMixin,forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('company_name', 'industry', 'phone_number','website','company_info','profile_photo')

class UpdateJobseekerForm(ProfilePhotoMixin,forms.ModelForm):
    
    class Meta:
        model = JobSeeker
        fields = ('phone_number','first_name','last_name','profile_photo')