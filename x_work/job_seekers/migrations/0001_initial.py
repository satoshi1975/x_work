# Generated by Django 4.2.1 on 2023-07-08 16:02

from django.db import migrations, models
import job_seekers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(default=None, max_length=150, null=True)),
                ('bio', models.TextField(blank=True, default=None, null=True)),
                ('education', models.CharField(choices=[('none', 'Without education'), ('bachelor', "Bachelor's Degree"), ('master', "Master's Degree"), ('doctorate', 'Doctorate Degree'), ('license', 'Professional Certification/License'), ('courses', 'Courses/Training'), ('hight', 'hight school')], default=None, max_length=10, null=True)),
                ('schedule', models.CharField(choices=[('none', "doesn't matter"), ('full', 'full-time'), ('flex', 'flexible'), ('shift', 'shift'), ('part', 'part-time'), ('seasonal', 'seasonal'), ('hybrid', 'hybrid')], default=None, max_length=10, null=True)),
                ('salary', models.IntegerField(blank=True, default=None, null=True)),
                ('key_skills', models.TextField(blank=True, default=None, null=True)),
                ('work_place', models.CharField(choices=[('none', "doesn't matter"), ('full', 'full-time'), ('flex', 'flexibility'), ('home', 'from home')], default=None, max_length=4, null=True)),
                ('experience', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=500)),
                ('study_start', models.DateField(default=None)),
                ('study_end', models.DateField(default=None)),
            ],
            options={
                'default_related_name': 'cv_education',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('start_work', models.DateField(default=None, null=True)),
                ('end_work', models.DateField(default=None, null=True)),
            ],
            options={
                'default_related_name': 'cv_experience',
            },
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('profile_photo', models.ImageField(default=None, upload_to=job_seekers.models.JobSeeker.image_upload_to)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('date_of_birth', models.DateField(default=None, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(default=None, max_length=255)),
            ],
        ),
    ]
