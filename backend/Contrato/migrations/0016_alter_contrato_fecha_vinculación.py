# Generated by Django 4.1.3 on 2023-01-04 01:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contrato', '0015_alter_contrato_fecha_vinculación'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='fecha_vinculación',
            field=models.DateField(default=datetime.datetime(2023, 1, 4, 1, 13, 34, 871170, tzinfo=datetime.timezone.utc)),
        ),
    ]
