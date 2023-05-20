from django.shortcuts import render, redirect
from main.forms import RegistrationForm, LoginForm
from main.services import UserService, UserData, UpdateUserData
from employers.models import Employer                                                     
from job_seekers.models import JobSeeker                                                     
from main.models import User   

def main_page(request):

    return render(request, 'main_page.html')

def profile(request):
    if request.method=='POST':
        UpdateUserData().update_child_model(request)
        context=UserData().return_context_for_user_profile(request)
        return render(request, 'user_profile.html', context)
    else:
        context=UserData().return_context_for_user_profile(request)
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


def geoform(request):
    return render(request,'geoform.html')