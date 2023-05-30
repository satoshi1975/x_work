from django.db import models
from uuid import uuid4
from main.models import User,Cities,Occupation
from django.contrib.postgres.fields import DateTimeRangeField

# from main import models as model


class JobSeeker(models.Model):
    def image_upload_to(instance, filename):
    # Генерация уникального имени файла
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        # Возвращение пути сохранения файла
        return f'job_seekers_photos/{filename}'
    id = models.BigAutoField(primary_key=True)
    profile_photo=models.ImageField(upload_to=image_upload_to, default=None)
    user=models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    first_name=models.CharField(max_length=50, blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    city=models.ForeignKey(Cities, on_delete=models.CASCADE, blank=True, default=None)
    email=models.EmailField(max_length=255,default=None)

    def __str__(self):
        return str(self.id)


class CV(models.Model):
    SCHEDULE=[
        ("none","doesn't matter"),
        ('full','full-time'),
        ('flex','flexible'),
        ('shift','shift'),
        ('part','part-time'),
        ('seasonal','seasonal'),
        ('hybrid','hybrid')
    ]
    WORK_PLACE=[
        ('none',"doesn't matter"),
        ('full','full-time'),
        ('flex','flexibility'),
        ('home','from home'),
    ]
    EDUCATION=[
        ('none',"Without education"),
        ('bachelor',"Bachelor's Degree"),
        ('master',"Master's Degree"),
        ('doctorate',"Doctorate Degree"),
        ('license',"Professional Certification/License"),
        ('courses','Courses/Training'),
        ('hight',"hight school")
    ]
    jobseeker=models.ForeignKey(JobSeeker, on_delete=models.CASCADE,default=None)
    occupation=models.CharField(max_length=150, default=None, null=True)
    bio=models.TextField(default=None, blank=True, null=True)
    education=models.CharField(max_length=10,choices=EDUCATION,default=None, null=True)
    schedule=models.CharField(max_length=10,default=None,choices=SCHEDULE, null=True)
    salary=models.IntegerField(blank=True,default=None, null=True)
    key_skills=models.TextField(blank=True,default=None, null=True)
    work_place=models.CharField(max_length=4, choices=WORK_PLACE, default=None, null=True)
    # city=models.ForeignKey(Cities, on_delete=models.CASCADE,default=None, blank=True)

    def __str__(self):
        return str(self.occupation)

class Experience(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,related_name='cv_experience',default=None)
    occupation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_work = models.DateField(default=None)
    end_work = models.DateField(default=None)

    class Meta:
        default_related_name = 'cv_experience'

    def __str__(self):
        return self.occupation

class Education(models.Model):
    cv=models.ForeignKey(CV, on_delete=models.CASCADE,related_name='cv_education',default=None)
    institution=models.CharField(max_length=500)
    study_start=models.DateField(default=None)
    study_end=models.DateField(default=None)

    class Meta:
        default_related_name = 'cv_education'

    def __str__(self):
        return self.institution