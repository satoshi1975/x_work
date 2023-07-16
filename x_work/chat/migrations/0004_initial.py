# Generated by Django 4.2.1 on 2023-07-08 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocklist',
            name='blocked_user',
            field=models.ManyToManyField(related_name='blocked_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blocklist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]