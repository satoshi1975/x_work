# Generated by Django 4.2.1 on 2023-05-25 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0011_jobseeker_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='username',
        ),
    ]
