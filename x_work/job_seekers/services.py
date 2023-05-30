from job_seekers.models import CV, JobSeeker,Education,Experience
from main.models import User
from job_seekers.forms import CVForm
import json
from itertools import zip_longest

def get_context_cv_list(user_id):
    user=User.objects.get(id=user_id)
    jobseeker=JobSeeker.objects.filter(user=user)
    list_of_cv=CV.objects.filter(jobseeker=jobseeker)
    
    return list_of_cv

def get_data_from_post(request):
    print(request.body)
    postdata = json.loads(request.POST.decode('utf-8'))
    data={}
    for key, value in postdata.items():
        data[key] = value
    return data


class CVEditor:
    
    @staticmethod
    def get_jobseeker(request):
        return JobSeeker.objects.get(user_id=request.user.id)

    @staticmethod
    def update_cv(data,model_instance):
        form=CVForm(data=data,instance=model_instance)
        if form.is_valid():
            form.save()
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
        jobseeker = JobSeeker.objects.get(user_id=request.user.id)
        cv=CV.objects.create(jobseeker=jobseeker)
        CVEditor().update_cv(request.POST,cv)
        
        if len(request.POST.getlist('institution'))!=0:
            CVEditor().create_education_objects(request, cv)
        if len(request.POST.getlist('company'))!=0:
            CVEditor().create_experience_objects(request, cv)
        return True

    @staticmethod
    def create_experience_objects(request,cv):
        company=request.POST.getlist('company')
        position=request.POST.getlist('position')
        work_start=request.POST.getlist('work_start')
        work_end=request.POST.getlist('work_end')
        for company, position, work_start, work_end in zip_longest(company,position,work_start,work_end):
            experience_entry= Experience(cv=cv, occupation=position, company=company, start_work=work_start,end_work=work_end)
            experience_entry.save()
        return True


    @staticmethod
    def create_education_objects(request,cv):
        institution=request.POST.getlist('institution')
        study_start=request.POST.getlist('study_start')
        study_end=request.POST.getlist('study_end')
        
        # max_length = max(len(university), len(study_start), len(study_end))

        for institution, start, end in zip_longest(institution, study_start, study_end):
            education_entry = Education(cv=cv,institution=institution, study_start=start, study_end=end)
            education_entry.save()

        return True

class CVShow:


    @staticmethod
    def get_context_user_cv_list(request):
        
        pass