from job_seekers.models import CV, JobSeeker
from main.models import User
from job_seekers.forms import CVForm

def get_context_cv_list(user_id):
    user=User.objects.get(id=user_id)
    jobseeker=JobSeeker.objects.filter(user=user)
    list_of_cv=CV.objects.filter(jobseeker=jobseeker)
    
    return list_of_cv


class CreateCV:
    @staticmethod
    def create_cv(request):
        jobseeker = JobSeeker.objects.get(user_id=request.user.id)
        print(jobseeker)
        form = CVForm(data=request.POST)
        form.jobseeker=jobseeker
        print(form.data,'afafaf')
        form.save()
        
        
        return True
        # else:
        #     errors = form.errors.as_data()
        #     for field, error_list in errors.items():
        #         print(f"Поле {field}:")
        #         for error in error_list:
        #             print(f"- {error}")
        #     return False
