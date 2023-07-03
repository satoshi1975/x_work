#business logic for managing applicant profiles
from job_seekers.models import CV, JobSeeker,Education,Experience
from employers.models import Vacancy
from django.db.models import Q
from main.models import User, Cities
from job_seekers.forms import CVForm
import json
from itertools import zip_longest
from datetime import date

def get_context_cv_list(user_id):
    '''get a list of resumes'''
    jobseeker=JobSeeker.objects.get(user_=user_id)
    list_of_cv=CV.objects.filter(jobseeker=jobseeker)
    
    return list_of_cv

# def get_data_from_post(request):
    
#     postdata = json.loads(request.POST.decode('utf-8'))
#     data={}
#     for key, value in postdata.items():
#         data[key] = value
#     return data

def get_user_age(birth_date):
    '''Getting the age of the user'''
    today = date.today()
    age = today.year - birth_date.year

    # Checking if it's already been a birthday this year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1

    return age

def reply_to_vacancy(request,vacancy_id):
    '''reply to the job'''
    vacancy= Vacancy.objects.get(id = vacancy_id)
    jobseeker = JobSeeker.objects.get(user=request.user)
    if jobseeker in vacancy.feedback.all():
        pass
    else:
        vacancy.feedback.set([jobseeker])
        

class CVEditor:
    '''Editing Resume Data'''
    @staticmethod
    def get_jobseeker(request):
        '''get the job seeker from the request'''
        return JobSeeker.objects.get(user_id=request.user.id)

    @staticmethod
    def delete_cv(request):
        '''delete cv by id'''
        cv_id=request.POST['cv_id']
        CV.objects.get(id=cv_id).delete()
        return True

    @staticmethod
    def update_cv(data,model_instance):
        '''update cv data'''
        form=CVForm(data=data,instance=model_instance)
        
        if form.is_valid():
            form.save()
            if data['city_id'] and data['city_id']!='None':
                model_instance.city=Cities.objects.get(id=data['city_id'])
                model_instance.save()
            return True
        
        
        else:
            errors = form.errors.as_data()
            for field, error_list in errors.items():
                print(f"Поле {field}:")
                for error in error_list:
                    print(f"- {error}")
            return False

        

    @staticmethod
    def create_cv(request):
        '''create new resume'''
        jobseeker = JobSeeker.objects.get(user_id=request.user.id)
        cv=CV.objects.create(jobseeker=jobseeker)
        CVEditor().update_cv(request.POST,cv)
        
        if len(request.POST.getlist('institution'))!=0:
            CVEditor().create_education_objects(request, cv, edit=False)
        if len(request.POST.getlist('company'))!=0:
            CVEditor().create_experience_objects(request, cv, edit=False)
        return True
    
    @staticmethod
    def edit_cv(request,cv_id):
        '''Edit resume'''
        cv=CV.objects.get(id=cv_id)
        CVEditor().update_cv(request.POST, cv)
        # if len(request.POST.getlist('institution'))!=0:
        CVEditor().create_education_objects(request, cv, edit=True)
        # if len(request.POST.getlist('company'))!=0:
        CVEditor().create_experience_objects(request, cv, edit=True)
        return True


    @staticmethod
    def create_experience_objects(request,cv, edit):
        '''create experience entry'''
        if edit:
            Experience.objects.filter(cv_id=cv.id).delete()
        company=request.POST.getlist('company')
        
        position=request.POST.getlist('position')
        
        work_start=request.POST.getlist('work_start')
        
        work_end=request.POST.getlist('work_end')
        
        for company, position, work_start, work_end in zip_longest(company,position,work_start,work_end):
            experience_entry= Experience(cv=cv, occupation=position, company=company, start_work=work_start,end_work=work_end)
            experience_entry.save()
        return True


    @staticmethod
    def create_education_objects(request,cv,edit):
        '''create education entry'''
        if edit:
            Education.objects.filter(cv_id=cv.id).delete()
        institution=request.POST.getlist('institution')
        study_start=request.POST.getlist('study_start')
        study_end=request.POST.getlist('study_end')
        
        for institution, start, end in zip_longest(institution, study_start, study_end):
            education_entry = Education(cv=cv,institution=institution, study_start=start, study_end=end)
            education_entry.save()

        return True

class CVShow:
    '''resume data display'''
    @staticmethod
    def get_context_user_cv_list(user_id):
        '''get cv list by user'''
        user=User.objects.get(id=user_id)

        jobseeker=JobSeeker.objects.get(user=user)
        list_of_cv=CV.objects.filter(jobseeker=jobseeker)
        return list_of_cv

    @staticmethod
    def get_context_user_cv_show(cv_id):
        '''get cv data'''
        cv=CV.objects.prefetch_related('cv_education','cv_experience').get(id=cv_id)
        user_id=cv.jobseeker.user.id
        user_age=get_user_age(cv.jobseeker.get_date())
        context={
            'cv':cv,
            'user_id':user_id,
            'user_age':user_age
        }   
        return context
    


# class VacancySearchService:
#     @staticmethod
#     def search_vacancies(form_data):
#         query = Vacancy.objects.all()
        
#         search_fields = {
#             'occupation': 'occupation__icontains',
#             'city': 'city__icontains',
#             'schedule': 'schedule',
#             'experience': 'experience__gte',
#             'education': 'education',
#             'salary': 'salary__gte',
#             'work_place': 'work_place',
#             'job_description': 'job_description__icontains',
#             # 'key_skills': 'key_skills__icontains',
#         }
        
#         conditions = Q()
        
#         for field, lookup in search_fields.items():
#             value = form_data.get(field)
#             if value:
#                 conditions |= Q(**{lookup: value})
        
#         query = query.filter(conditions)
        
#         return query 