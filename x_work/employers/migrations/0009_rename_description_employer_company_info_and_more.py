# Generated by Django 4.2.1 on 2023-05-22 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0008_employer_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employer',
            old_name='description',
            new_name='company_info',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='description',
            new_name='job_description',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='work',
            new_name='job_title',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='address',
        ),
    ]
