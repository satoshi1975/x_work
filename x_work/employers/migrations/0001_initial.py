# Generated by Django 4.2.1 on 2023-07-08 16:02

from django.db import migrations, models
import employers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(default=None, upload_to=employers.models.Employer.image_upload_to)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_info', models.TextField(blank=True, null=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(default=None, max_length=500, null=True)),
                ('schedule', models.CharField(choices=[('none', "doesn't matter"), ('full', 'full-time'), ('flex', 'flexible'), ('shift', 'shift'), ('part', 'part-time'), ('seasonal', 'seasonal'), ('hybrid', 'hybrid')], default=None, max_length=10, null=True)),
                ('experience', models.IntegerField(blank=True, default=None, null=True)),
                ('education', models.CharField(choices=[('none', 'Without education'), ('bachelor', "Bachelor's Degree"), ('master', "Master's Degree"), ('doctorate', 'Doctorate Degree'), ('license', 'Professional Certification/License'), ('courses', 'Courses/Training'), ('hight', 'hight school')], max_length=10, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('work_place', models.CharField(choices=[('none', "doesn't matter"), ('full', 'full-time'), ('flex', 'flexibility'), ('home', 'from home')], default=None, max_length=4, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('key_skills', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
