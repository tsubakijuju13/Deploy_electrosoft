# Generated by Django 4.1.3 on 2023-01-04 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contrato', '0017_alter_contrato_fecha_vinculación'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='fecha_vinculación',
            field=models.DateField(default=datetime.datetime(2023, 1, 4, 2, 12, 15, 265153, tzinfo=datetime.timezone.utc)),
        ),
    ]
