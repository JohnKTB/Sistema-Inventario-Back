# Generated by Django 3.1.7 on 2021-02-25 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0003_auto_20210223_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Estado Fabricante'),
        ),
    ]
