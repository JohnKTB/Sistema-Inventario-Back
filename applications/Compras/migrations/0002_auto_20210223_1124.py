# Generated by Django 3.1.7 on 2021-02-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricante',
            name='estado',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Estado Fabricante'),
        ),
    ]
