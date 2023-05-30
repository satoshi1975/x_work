# Generated by Django 4.2.1 on 2023-05-30 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0025_alter_cv_bio_alter_cv_education_alter_cv_key_skills_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='study_period',
        ),
        migrations.AddField(
            model_name='education',
            name='cv',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cv_education', to='job_seekers.cv'),
        ),
        migrations.AddField(
            model_name='education',
            name='study_end',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='education',
            name='study_start',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cv_experience', to='job_seekers.cv'),
        ),
    ]
