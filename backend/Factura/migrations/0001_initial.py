# Generated by Django 4.1.4 on 2023-01-02 19:56

import Factura.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Contrato', '0005_alter_contrato_fecha_vinculación'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('no_factura', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_expedicion', models.DateField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateField()),
                ('estado', models.CharField(default='En mora', max_length=20)),
                ('codigo_contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contrato.contrato')),
            ],
            options={
                'db_table': 'Factura',
            },
        ),
        migrations.CreateModel(
            name='DetallesFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumo_acueducto', models.FloatField()),
                ('acueducto_lectura_actual', models.CharField(max_length=20)),
                ('acueducto_lectura_anterior', models.CharField(default='0.0', max_length=20)),
                ('acueducto_valor_total', models.FloatField(validators=[Factura.models.valid_cost_service])),
                ('alcantarillado_valor_total', models.FloatField(validators=[Factura.models.valid_cost_service])),
                ('consumo_energia', models.FloatField()),
                ('energia_lectura_actual', models.CharField(max_length=20)),
                ('energia_lectura_anterior', models.CharField(default='0.0', max_length=20)),
                ('energia_valor_total', models.FloatField(validators=[Factura.models.valid_cost_service])),
                ('lys_valor_total', models.FloatField(validators=[Factura.models.valid_cost_service])),
                ('alumbrado_valor_total', models.FloatField(validators=[Factura.models.valid_cost_service])),
                ('pago_total', models.FloatField()),
                ('factura', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Factura.factura')),
            ],
            options={
                'db_table': 'DetallesFactura',
            },
        ),
    ]
