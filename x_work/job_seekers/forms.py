from django import forms
from job_seekers.models import CV, JobSeeker
from employers.models import Vacancy
class CVForm(forms.ModelForm):
    '''form for creating summary'''
    class Meta:
        model = CV
        exclude = ['jobseeker','city']



class VacancySearchForm(forms.Form):
    '''form for search vacancy'''
    occupation = forms.CharField(label='Occupation', required=False)
    city = forms.CharField(label='City', required=False)
    schedule = forms.ChoiceField(label='Schedule', choices=Vacancy.SCHEDULE, required=False)
    experience = forms.IntegerField(label='Experience', required=False)
    education = forms.ChoiceField(label='Education', choices=Vacancy.EDUCATION, required=False)
    salary = forms.IntegerField(label='Salary', required=False)
    work_place = forms.ChoiceField(label='Work Place', choices=Vacancy.WORK_PLACE, required=False)
    job_description = forms.CharField(label='Job Description', required=False)
    