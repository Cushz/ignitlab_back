# Generated by Django 4.1.7 on 2023-03-05 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('igniteapp', '0003_investor_user_alter_startup_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='user',
        ),
        migrations.AlterField(
            model_name='startup',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='startups', to=settings.AUTH_USER_MODEL),
        ),
    ]
