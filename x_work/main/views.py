from django.shortcuts import render, redirect
from main.forms import RegistrationForm, LoginForm
from main.services import UserService, UserData, UpdateUserData,MainPageContent,EmployersJobseekerContext,ArticlesContext
from employers.models import Employer                                                     
from job_seekers.models import JobSeeker     
from main.models import User, Cities, Occupation
from django.http import JsonResponse
from django.db.models import Q





def main_page(request):
    context= MainPageContent().get_main_page_content()    
    print(context)
    return render(request, 'main_page.html',context=context)

def profile(request):
    if request.method=='POST':
        # print(request.POST,'adadad')
        UpdateUserData().update_child_model(request)
        context=UserData().return_context_for_user_profile(request)
        return render(request, 'user_profile.html', context)
    else:
        context=UserData().return_context_for_user_profile(request)
        print(context)
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


# 
def log_out(request):
    UserService().logout_user(request)
    return render(request,'main_page.html')

def get_city(request):
    search=request.GET.get('search').capitalize()
    payload=[]
    if search:
        objs=Cities.objects.filter(city__startswith = search)[:3]
        
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

# from django.shortcuts import render

# def chat_room(request, user_id):
#     return render(request, "chat_room.html", {"user_id": user_id})
def show_profile(request,user_id):
    context = EmployersJobseekerContext().get_profile_context(user_id)
    if context['user_type'] == 'jobseeker':
        return render(request, 'jobseeker_profile.html', context)
    else:
        return render(request, 'employer_profile.html', context)

# def employer_profile(request,user_id):
#     context = EmployersJobseekerContext().get_jobseeker_context(user_id)
#     return render(request, 'employer_profile.html', context)

def show_articles_list(request,article_id):
    articles_list=ArticlesContext().get_articles_list()
    if article_id == 0:
        return render(request, 'articles.html',context={'articles_list':articles_list})
    else:
        return render(request, 'articles.html',context={'articles_list':articles_list,'article_id':article_id})

