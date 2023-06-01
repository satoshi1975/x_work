from django import forms
from job_seekers.models import CV, JobSeeker

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        exclude = ['jobseeker']
   