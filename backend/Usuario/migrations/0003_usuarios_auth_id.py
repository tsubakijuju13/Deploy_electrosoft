# Generated by Django 4.1.3 on 2023-01-04 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Usuario', '0002_ju'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='auth_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
