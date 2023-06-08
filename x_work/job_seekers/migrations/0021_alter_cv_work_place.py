# Generated by Django 4.2.1 on 2023-05-29 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0020_cv_work_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='work_place',
            field=models.CharField(choices=[('none', "doesn't matter"), ('full', 'full-time'), ('flex', 'flexibility'), ('home', 'from home')], default=None, max_length=4),
        ),
    ]