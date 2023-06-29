from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from main.forms import RegistrationForm, LoginForm, UpdateEmployerForm, UpdateJobseekerForm
from employers.models import Employer,Vacancy                                               
from job_seekers.models import JobSeeker,CV
from job_seekers import services as jobseeker_services
from main.models import User, Cities, Articles                                                

class UserService:

    @staticmethod
    def add_new_user_by_type(data):
        user = User.objects.get(email=data['email'])
        city=Cities.objects.get(id=int(data['city_id']))
        user.user_type=data['user_type']
        user.save()
        if data['user_type'] == 'company':
            employer = Employer.objects.create(user=user,
                                            company_name=data['company_name'],
                                            phone_number=data['phone_number'],
                                            email=data['email'],
                                            city=city)
            employer.profile_photo='employers_photos/default_profile_img.jpg'
            employer.save()
        elif data['user_type'] == 'jobseeker':
            jobseeker = JobSeeker.objects.create(user=user,
                                                first_name=data['first_name'],
                                                last_name=data['last_name'],
                                                phone_number=data['phone_number'],
                                                email=data['email'],
                                                city=city)
            jobseeker.profile_photo='job_seekers_photos/default_profile_img.jpg'
            jobseeker.save()
        
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
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return True
        else:
            return False

    @staticmethod
    def logout_user(request):
        logout(request)

class UserData:
    
    @staticmethod
    def return_context_for_user_profile(request):
        user = User.objects.get(email=request.user)
        user_type = User.objects.filter(email=request.user).values_list('user_type', flat=True)[0]
        context = {'user': user}
        if user_type=='jobseeker':
            jobseeker=JobSeeker.objects.get(user=user)
            context['user_fields']=jobseeker
        elif user_type=='company':
            employer=Employer.objects.get(email=user)
            context['user_fields']=employer
        form=UpdateJobseekerForm()
        context['form']=form

        return context


class UpdateUserData:

    @staticmethod
    def update_child_model(request):
        user_type = User.objects.filter(email=request.user).values_list('user_type', flat=True)[0]
        city=Cities.objects.get(id=request.POST['city_id'])
        if user_type=='jobseeker':
        
            user=JobSeeker.objects.get(user=request.user)
            form=UpdateJobseekerForm(request.POST,request.FILES, instance=user)
        elif user_type=='company':

            user=Employer.objects.get(user=request.user)

            form=UpdateEmployerForm(request.POST,request.FILES, instance=user)  
        user.city=city
        if form.is_valid():
            
            form.save()

            return True
        else:
            # errors = data.errors.as_data()
            # for field, error_list in errors.items():
            #     # Выводим имя поля и соответствующие сообщения об ошибках
            #     print(f"Поле {field}:")
            #     for error in error_list:
            #         print(f"- {error}")
            return False
        


class MainPageContent:



    @staticmethod
    def get_main_page_content():
        summary=CV.objects.order_by('?').first()
        job=Vacancy.objects.order_by('?').first()
        company=Employer.objects.order_by('?').first()
        articles=Articles.objects.order_by('?')[:3]
        context={
            'summary':summary,
            'job':job,
            'company': company,
            'articles': articles,
        }
        return context

class EmployersJobseekerContext:


    @staticmethod
    def get_profile_context(user_id):
        user=User.objects.get(id=user_id)
        if user.user_type == 'jobseeker':
            jobseeker=JobSeeker.objects.get(user=user)
            jobseeker_age=jobseeker_services.get_user_age(jobseeker.get_date())
            cv_list=CV.objects.filter(jobseeker=jobseeker)
            context={
                'user_type':'jobseeker',
                'jobseeker':jobseeker,
                'jobseeker_age':jobseeker_age,
                'cv_list': cv_list
            }
        else:
            employer=Employer.objects.get(user=user)
            job_list=Vacancy.objects.filter(employer=employer)
            context={
                'user_type':'employer',
                'employer':employer,
                'job_list':job_list
            }
        return context

class ArticlesContext:


    def get_articles_list(request):
        return Articles.objects.all()
    
    def get_article(article_id):
        return Articles.objects.get(id=article_id)