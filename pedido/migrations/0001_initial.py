# Generated by Django 5.1.3 on 2024-11-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_pedido', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('em_preparo', 'Em_preparo'), ('a_caminho', 'A_caminho'), ('entregue', 'Entregue')], max_length=15)),
            ],
        ),
    ]
