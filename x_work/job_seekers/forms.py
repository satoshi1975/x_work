from django import forms
from job_seekers.models import CV, JobSeeker

class CVForm(forms.ModelForm):
    jobseeker=forms.ModelChoiceField(queryset=JobSeeker.objects.all())

    class Meta:
        model = CV
        # exclude = ['jobseeker']
        fields=['occupation','jobseeker']

    