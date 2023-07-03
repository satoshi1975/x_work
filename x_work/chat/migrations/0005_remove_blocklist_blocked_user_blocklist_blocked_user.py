# Generated by Django 4.2.1 on 2023-06-30 11:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0004_blocklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blocklist',
            name='blocked_user',
        ),
        migrations.AddField(
            model_name='blocklist',
            name='blocked_user',
            field=models.ManyToManyField(related_name='blocked_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
