# Generated by Django 4.2.1 on 2023-05-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0011_vacancy_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='profile_photo',
            field=models.ImageField(default=None, upload_to='employers_photos/'),
        ),
    ]
