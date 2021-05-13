# Generated by Django 3.1.7 on 2021-04-06 04:35

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('IGV', models.FloatField(default=0.18, verbose_name='IGV')),
                ('nombreCli', models.CharField(blank=True, default='', max_length=100, verbose_name='Nombre Cliente')),
                ('precioT', models.PositiveIntegerField(blank=True, default=0, verbose_name='Precio Total de la venta')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
            ],
            options={
                'verbose_name': 'testT',
                'verbose_name_plural': 'testTs',
                'db_table': 'testT',
            },
        ),
    ]
