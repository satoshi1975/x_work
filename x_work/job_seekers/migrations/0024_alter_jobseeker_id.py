# Generated by Django 4.2.1 on 2023-05-29 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0023_remove_cv_city_alter_cv_bio_alter_cv_occupation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
