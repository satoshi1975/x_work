# Generated by Django 4.2.1 on 2023-06-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0019_alter_vacancy_city_alter_vacancy_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='city',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='occupation',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
