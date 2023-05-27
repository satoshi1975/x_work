from django.db import models
from uuid import uuid4
from main.models import User,Cities,Occupation

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
        return self.user


class CV(models.Model):
    JOB_EXPERIENCE=[
        ('none','without'),
        ('1','1 year'),
        ('13','1-3 year'),
        ('3','3 year'),
        ('5','5 year')
    ]
    SCHEDULE=[
        ('full','full-time'),
        ('flex','flexible'),
        ('shift','shift'),
        ('part','part-time'),
        ('seasonal','seasonal'),
        ('hybrid','hybrid')
    ]
    WORK_PLACE=[
        ('full','full-time'),
        ('flex','flexibility'),
        ('home','from home'),
    ]
    EDUCATION=[
        ('bachelor',"Bachelor's Degree"),
        ('master',"Master's Degree"),
        ('doctorate',"Doctorate Degree"),
        ('license',"Professional Certification/License"),
        ('courses','Courses/Training'),
        ('hight',"hight school")
    ]
    jobseeker=models.ForeignKey(JobSeeker, on_delete=models.CASCADE,default=None)
    occupation=models.ForeignKey(Occupation, on_delete=models.CASCADE,default=None)
    city=models.ForeignKey(Cities, on_delete=models.CASCADE,default=None)
    standing=models.CharField(max_length=4,default='none',choices=JOB_EXPERIENCE)
    education=models.CharField(max_length=10,choices=EDUCATION,default=None)
    schedule=models.CharField(max_length=10,default=None,choices=SCHEDULE)
    salary=models.IntegerField(blank=True,default=None)
    experience=models.TextField(default=None)
    key_skills=models.TextField(blank=True,default=None)