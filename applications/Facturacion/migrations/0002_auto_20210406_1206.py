# Generated by Django 3.1.7 on 2021-04-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='precioT',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio Venta'),
        ),
    ]
