from django import forms
from job_seekers.models import CV, JobSeeker

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        exclude = ['jobseeker']
        # fields=['occupation','bio','education','schedule','salary','key_skills','work_place']
    # def __init__(self, *args, **kwargs):
    #     jobseeker = kwargs.pop('jobseeker', None)
    #     super(CVForm, self).__init__(*args, **kwargs)
    #     self.jobseeker = jobseeker

    