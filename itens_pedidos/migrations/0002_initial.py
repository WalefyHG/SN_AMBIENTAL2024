# Generated by Django 5.1.3 on 2024-11-08 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itens_pedidos', '0001_initial'),
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itenspedidos',
            name='pedido_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido'),
        ),
    ]
