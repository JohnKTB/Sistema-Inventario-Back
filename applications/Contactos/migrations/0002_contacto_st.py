# Generated by Django 3.1.7 on 2021-03-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contactos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='st',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Estado Contacto'),
        ),
    ]