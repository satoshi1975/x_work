# Generated by Django 4.2.1 on 2023-06-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0029_cv_experience_alter_experience_end_work_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='experience',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
