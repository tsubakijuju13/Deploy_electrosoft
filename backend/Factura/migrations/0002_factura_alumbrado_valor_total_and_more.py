# Generated by Django 4.1.3 on 2023-01-03 01:55

import Factura.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Factura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='alumbrado_valor_total',
            field=models.FloatField(null=True, validators=[Factura.models.valid_cost_service]),
        ),
        migrations.AddField(
            model_name='factura',
            name='consumo_energia',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='factura',
            name='energia_lectura_actual',
            field=models.CharField(default='0.0', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='factura',
            name='energia_valor_total',
            field=models.FloatField(null=True, validators=[Factura.models.valid_cost_service]),
        ),
        migrations.AddField(
            model_name='factura',
            name='lys_valor_total',
            field=models.FloatField(null=True, validators=[Factura.models.valid_cost_service]),
        ),
        migrations.AddField(
            model_name='factura',
            name='pago_total',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='DetallesFactura',
        ),
    ]
