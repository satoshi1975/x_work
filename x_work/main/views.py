from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from main.forms import RegistrationForm, LoginForm
from main.services import UserService, UserData, UpdateUserData,MainPageContent,EmployersJobseekerContext,ArticlesContext
from employers.models import Employer                                                     
from job_seekers.models import JobSeeker     
from main.models import User, Cities, Occupation
from django.http import JsonResponse
from django.db.models import Q





def main_page(request):
    """
    Display the home page
    """
    context= MainPageContent().get_main_page_content()    
    return render(request, 'main_page.html',context=context)

def profile(request):
    '''Display or change the main data of the user's profile'''
    if request.method=='POST':
        UpdateUserData().update_child_model(request) # Update job seeker/employer data
        context=UserData().return_context_for_user_profile(request) #Get updated user data
        return render(request, 'user_profile.html', context)
    else:
        context=UserData().return_context_for_user_profile(request) #Get user data
        return render(request, 'user_profile.html', context)

def register(request):
    '''display the registration page and accept data for registration'''
    if request.method == 'POST':
        print('POST')
        print(request.POST)
        if UserService().register_user(request, request.POST): #accept data and create a user 
            return render(request, 'main_page.html')
        else:
            form = RegistrationForm() 
            return render(request, 'signup.html', {'form': form})

    else:
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form})

def log_in(request):
    '''display the authentication page and accept login information'''
    if request.method == 'POST':
        if UserService().login_user(request, request.POST): #user authentication
            return redirect(reverse('main_page'))

        else:
            messages.error(request, 'Некорректные учетные данные. Пожалуйста, повторите вход.')
    form=LoginForm()
    return render(request,'login.html',{'form': form})



def log_out(request):
    '''log out user'''
    UserService().logout_user(request)
    return redirect(reverse('main_page'))

def get_city(request):
    '''get a city to auto-complete as you enter'''
    search=request.GET.get('search').capitalize()
    payload=[]
    if search:
        objs=Cities.objects.filter(city__startswith = search)[:3]
        print('OBJ')
        print(Cities.objects.all()[:3])
        for obj in objs:
            payload.append({
                'city' : obj.city,
                'state': obj.state_name,
                'id':obj.id
            })
    return JsonResponse({
        'status' : True,
        'payload': payload
    })

def get_occupation(request):
    '''get a profession to auto-complete as you enter'''
    search=request.GET.get('search').capitalize()
    payload=[]
    if search:
        objs=Occupation.objects.filter(Q(occupation__startswith = search) | Q(occupation__contains = search))[:3]
        for obj in objs:
            payload.append({
                'id' : obj.id,
                'occupation': obj.occupation
            })
    return JsonResponse({
        'status' : True,
        'payload': payload
    })


def show_profile(request,user_id):
    '''Display the user profile depending on the type '''
    context = EmployersJobseekerContext().get_profile_context(user_id) 
    if context['user_type'] == 'jobseeker':
        return render(request, 'jobseeker_profile.html', context)
    else:
        return render(request, 'employer_profile.html', context)


def show_articles_list(request,article_id):
    '''Display a list of articles'''
    articles_list=ArticlesContext().get_articles_list()#Get a list of articles
    if article_id == 0:
        return render(request, 'articles.html',context={'articles_list':articles_list})
    else:
        return render(request, 'articles.html',context={'articles_list':articles_list,'article_id':article_id})
