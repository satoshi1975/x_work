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
    website = models.URLField(blank=True, null=True)
    city=models.ForeignKey(Cities, on_delete=models.CASCADE, default=None, null=True)


    def __str__(self):
        return self.company_name


class Vacancy(models.Model):
    SCHEDULE=[
        ('none',"doesn't matter"),
        ('full','full-time'),
        ('flex','flexible'),
        ('shift','shift'),
        ('part','part-time'),
        ('seasonal','seasonal'),
        ('hybrid','hybrid'),
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
        ('hight',"hight school"),
    ]

    
    employer=models.ForeignKey(Employer, on_delete=models.CASCADE)
    occupation=models.CharField(max_length=500,default=None, null=True)
    # city=models.CharField(max_length=500,default=None, null=True)
    city=models.ForeignKey(Cities, on_delete=models.CASCADE, blank=True, default=None, null=True)
    schedule=models.CharField(max_length=10,choices=SCHEDULE,default=None, null=True)
    experience=models.IntegerField(blank=True, default= None, null=True)
    education=models.CharField(max_length=10,choices=EDUCATION, null=True)
    salary=models.IntegerField(blank=True,null=True)
    work_place=models.CharField(max_length=4, choices=WORK_PLACE, default=None, null=True)
    job_description=models.TextField(blank=True, null=True)
    key_skills=models.TextField(blank=True, null=True)
    

    def __str__(self):
        return str(self.occupation)


