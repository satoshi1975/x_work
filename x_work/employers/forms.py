'''employer forms'''
from django import forms
from employers.models import Vacancy

class VacancyForm(forms.ModelForm):
    '''form for create or edit vacancy data'''
    class Meta:
        model = Vacancy
        exclude = ['employer','city']


class VacancySearchForm(forms.Form):
    '''form for vacancy searching'''
    occupation = forms.CharField(label='Occupation', required=False)
    city = forms.CharField(label='City', required=False)
    schedule = forms.ChoiceField(label='Schedule', choices=Vacancy.SCHEDULE, required=False)
    experience = forms.IntegerField(label='Experience', required=False)
    education = forms.ChoiceField(label='Education', choices=Vacancy.EDUCATION, required=False)
    salary = forms.IntegerField(label='Salary', required=False)
    work_place = forms.ChoiceField(label='Work Place', choices=Vacancy.WORK_PLACE, required=False)
    job_description = forms.CharField(label='Job Description', required=False)
    