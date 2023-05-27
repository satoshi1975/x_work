import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import User, Cities, Occupation
from uuid import uuid4

class Employer(models.Model):

    # def delete_old_profile_photo(self):
    #     if self.profile_photo:
    #         # Удаляем старый файл фото профиля
    #         os.remove(self.profile_photo.path)

    def image_upload_to(instance, filename):
        # Генерация уникального имени файла
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        # Возвращение пути сохранения файла
        return f'employers_photos/{filename}'

    profile_photo=models.ImageField(upload_to=image_upload_to, default=None)
    user=models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_info = models.TextField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    email=models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    # address = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    city=models.ForeignKey(Cities, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.company_name


class Vacancy(models.Model):
    SCHEDULE=[
        ('full','full-time'),
        ('flex','flexible'),
        ('shift','shift'),
        ('part','part-time'),
        ('seasonal','seasonal'),
        ('hybrid','hybrid')
    ]
    EDUCATION=[
        ('bachelor',"Bachelor's Degree"),
        ('master',"Master's Degree"),
        ('doctorate',"Doctorate Degree"),
        ('license',"Professional Certification/License"),
        ('courses','Courses/Training'),
        ('hight',"hight school")
    ]
    JOB_EXPERIENCE=[
        ('none','without'),
        ('1','1 year'),
        ('13','1-3 year'),
        ('3','3 year'),
        ('5','5 year')
    ]

    
    employer=models.ForeignKey(Employer, on_delete=models.CASCADE)
    occupation=models.ForeignKey(Occupation, on_delete=models.CASCADE,default=None)
    city=models.ForeignKey(Cities, on_delete=models.CASCADE,default=None)
    schedule=models.CharField(max_length=10,choices=SCHEDULE,default=None)
    experience=models.CharField(max_length=4,choices=JOB_EXPERIENCE)
    education=models.CharField(max_length=10,choices=EDUCATION)
    salary=models.IntegerField(blank=True)
    job_description=models.TextField(blank=True)
    key_skills=models.TextField(blank=True)


