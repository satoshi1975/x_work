# Generated by Django 4.2 on 2023-05-18 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0005_jobseeker_first_name_jobseeker_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
