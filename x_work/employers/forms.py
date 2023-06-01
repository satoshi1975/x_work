from django import forms
from employers.models import Employer, Vacancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ['employer']
   