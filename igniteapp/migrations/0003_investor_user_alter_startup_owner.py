# Generated by Django 4.1.7 on 2023-03-05 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('igniteapp', '0002_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='investor_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='startup',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_startups', to=settings.AUTH_USER_MODEL),
        ),
    ]