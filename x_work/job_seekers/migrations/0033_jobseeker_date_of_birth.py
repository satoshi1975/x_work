# Generated by Django 4.2.1 on 2023-06-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0032_alter_cv_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='date_of_birth',
            field=models.DateField(default=None, null=True),
        ),
    ]