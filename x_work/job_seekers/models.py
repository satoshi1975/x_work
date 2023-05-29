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
    
    profile_photo=models.ImageField(upload_to=image_upload_to, default=None)
    user=models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    first_name=models.CharField(max_length=50, blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    city=models.ForeignKey(Cities, on_delete=models.CASCADE, blank=True, default=None)
    email=models.EmailField(max_length=255,default=None)

    def __str__(self):
        return self.email


class CV(models.Model):
    # JOB_EXPERIENCE=[
    #     ('none','without'),
    #     ('1','1 year'),
    #     ('13','1-3 year'),
    #     ('3','3 year'),
    #     ('5','5 year')
    # ]
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
    # occupation=models.ForeignKey(Occupation, on_delete=models.CASCADE,default=None)
    occupation=models.CharField(max_length=150, default=None)
    bio=models.TextField(default=None, blank=True)
    # city=models.ForeignKey(Cities, on_delete=models.CASCADE,default=None, blank=True)
    education=models.CharField(max_length=10,choices=EDUCATION,default=None)
    schedule=models.CharField(max_length=10,default=None,choices=SCHEDULE)
    salary=models.IntegerField(blank=True,default=None)
    key_skills=models.TextField(blank=True,default=None)
    work_place=models.CharField(max_length=4, choices=WORK_PLACE, default=None)

    def __str__(self):
        return str(self.occupation)

class Experience(models.Model):
    
    resume = models.ForeignKey(CV, on_delete=models.CASCADE,related_name='resume',default=None)

    occupation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_work = models.DateField(default=None)
    end_work = models.DateField(default=None)

class Education(models.Model):
    institution=models.CharField(max_length=500)
    study_period=DateTimeRangeField()