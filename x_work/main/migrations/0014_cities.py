from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, null=True)),
                ('state_name', models.CharField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cities',
                # 'managed': False,
            },
        ),
    ]