# Generated by Django 4.2.1 on 2023-05-29 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0018_education_remove_cv_experience_remove_cv_standing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='Occupation',
            new_name='occupation',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='duration',
        ),
        migrations.AddField(
            model_name='experience',
            name='end_work',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='job_seekers.cv'),
        ),
        migrations.AddField(
            model_name='experience',
            name='start_work',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='cv',
            name='education',
            field=models.CharField(choices=[('none', 'Without education'), ('bachelor', "Bachelor's Degree"), ('master', "Master's Degree"), ('doctorate', 'Doctorate Degree'), ('license', 'Professional Certification/License'), ('courses', 'Courses/Training'), ('hight', 'hight school')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='cv',
            name='schedule',
            field=models.CharField(choices=[('none', "doesn't matter"), ('full', 'full-time'), ('flex', 'flexible'), ('shift', 'shift'), ('part', 'part-time'), ('seasonal', 'seasonal'), ('hybrid', 'hybrid')], default=None, max_length=10),
        ),
    ]
