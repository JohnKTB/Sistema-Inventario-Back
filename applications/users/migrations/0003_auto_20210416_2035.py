# Generated by Django 3.1.7 on 2021-04-17 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0002_auto_20210222_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='ApeMat',
            field=models.CharField(blank=True, max_length=30, verbose_name='Apellido Materno'),
        ),
        migrations.AddField(
            model_name='user',
            name='ApePat',
            field=models.CharField(blank=True, max_length=30, verbose_name='Apellido Paterno'),
        ),
        migrations.AddField(
            model_name='user',
            name='Nombres',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nombres'),
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=50, unique=True, verbose_name='Rol')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.rol'),
        ),
    ]