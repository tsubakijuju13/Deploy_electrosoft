# Generated by Django 4.1.3 on 2023-01-29 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contrato', '0021_alter_contrato_fecha_vinculación'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='departamento',
            field=models.CharField(default='Valle del cauca', max_length=50),
        ),
    ]