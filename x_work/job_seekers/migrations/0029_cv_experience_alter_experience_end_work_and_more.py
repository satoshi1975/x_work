# Generated by Django 4.2.1 on 2023-06-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0028_alter_education_options_alter_experience_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='experience',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_work',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_work',
            field=models.DateField(default=None, null=True),
        ),
    ]