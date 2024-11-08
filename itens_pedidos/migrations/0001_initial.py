# Generated by Django 5.1.3 on 2024-11-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItensPedidos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=90)),
                ('descricao', models.TextField(max_length=130)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=12)),
                ('categoria', models.CharField(choices=[('1', 'Bebida'), ('2', 'Sobremesa'), ('3', 'Salada'), ('4', 'Acompanhamento')], max_length=20)),
            ],
        ),
    ]
