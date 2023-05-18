from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from main.forms import RegistrationForm, LoginForm, CreateEmployerForm, CreateJobseekerForm
from employers.models import Employer                                                     
from job_seekers.models import JobSeeker                                                     
from main.models import User                                                     

class UserService:

    @staticmethod
    def add_new_user_by_type(data):
        user = User.objects.get(email=data['email'])
        user.user_type=data['user_type']
        user.save()
        if data['user_type'] == 'company':
            employer = Employer.objects.create(user=user,
                                            company_name=data['company_name'],
                                            phone_number=data['phone_number'],
                                            email=data['email'])
            employer.save()
        elif data['user_type'] == 'jobseeker':
            jobseeker = JobSeeker.objects.create(user=user,
                                                first_name=data['first_name'],
                                                last_name=data['last_name'],
                                                phone_number=data['phone_number'],
                                                email=data['email'])
            jobseeker.save()
        print('complete')
        return True

    @staticmethod
    def register_user(request, form_data):
        user = RegistrationForm(form_data)
        if user.is_valid():
            user.save()
            UserService.add_new_user_by_type(form_data)
            email = user.cleaned_data['email']
            password = user.cleaned_data['password1']
            user = authenticate(request, username=email, email=email, password=password)
            if user is not None:
                login(request, user)
                return True
        
        return False


    @staticmethod
    def login_user(request, form_data):
        email=form_data['username']
        password=form_data['password']
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return True
        else:
            return False

    @staticmethod
    def logout_user(request):
        logout(request)