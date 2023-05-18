from django.shortcuts import render, redirect
from main.forms import RegistrationForm, LoginForm
from main.services import UserService
from employers.models import Employer                                                     
from job_seekers.models import JobSeeker                                                     
from main.models import User   

def main_page(request):

    return render(request, 'main_page.html')

def profile(request):
    user = User.objects.get(email=request.user)
    user_type = User.objects.filter(email=request.user).values_list('user_type', flat=True)[0]
    context = {'user': user}
    if user_type=='jobseeker':
        jobseeker=JobSeeker.objects.get(user=user)
        context['user_fields']=jobseeker
    elif user_type=='company':
        employer=Employer.objects.get(email=user)
        print(employer)
        context['user_fields']=employer
    return render(request, 'user_profile.html', context)

def register(request):
    if request.method == 'POST':
        if UserService().register_user(request, request.POST):
            return render(request, 'main_page.html')
        else:
            form = RegistrationForm()
            return render(request, 'signup.html', {'form': form})

    else:
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        if UserService().login_user(request, request.POST):
            return render(request, 'main_page.html')

        else:
            
            form=LoginForm()
            return render(request,'login.html',{'form': form})
    else:
        form=LoginForm()
        return render(request,'login.html',{'form': form})



def log_out(request):
    UserService().logout_user(request)
    return render(request,'main_page.html')
