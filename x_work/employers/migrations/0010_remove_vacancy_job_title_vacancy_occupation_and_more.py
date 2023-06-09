# Generated by Django 4.2.1 on 2023-05-22 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_occupation_id'),
        ('employers', '0009_rename_description_employer_company_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='job_title',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='occupation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.occupation'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='schedule',
            field=models.CharField(choices=[('full', 'full-time'), ('flex', 'flexible'), ('shift', 'shift'), ('part', 'part-time'), ('seasonal', 'seasonal'), ('hybrid', 'hybrid')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='education',
            field=models.CharField(choices=[('bachelor', "Bachelor's Degree"), ('master', "Master's Degree"), ('doctorate', 'Doctorate Degree'), ('license', 'Professional Certification/License'), ('courses', 'Courses/Training'), ('hight', 'hight school')], max_length=10),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='experience',
            field=models.CharField(choices=[('none', 'without'), ('1', '1 year'), ('13', '1-3 year'), ('3', '3 year'), ('5', '5 year')], max_length=4),
        ),
    ]
