# Generated by Django 3.1.7 on 2021-03-13 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contactos', '0005_auto_20210312_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='st',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='st',
        ),
    ]