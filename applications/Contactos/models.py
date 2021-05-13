from django.db import models
from model_utils.models import TimeStampedModel


class Persona(TimeStampedModel):
    nombreEmp = models.CharField('Nombre Empresa', max_length=100, blank=True, default='')
    numeroImp = models.CharField('Numero de Impuesto', max_length=100, blank=True, default='')
    sitioWeb = models.CharField('Sitio Web', max_length=100, blank=True, default='')
    telefonoEmp = models.CharField('Telefono Empresa', max_length=100, blank=True, default='')
    ciudad = models.CharField('Ciudad', max_length=100, blank=True, default='')
    regionProvincia = models.CharField('Region/Provincia', max_length=100, blank=True, default='')
    codPostal = models.CharField('Codigo Postal', max_length=100, blank=True, default='')
    direccion = models.CharField('Direccion', max_length=100, blank=True, default='')
    created = models.DateTimeField('creado', auto_now_add=True)
    modified = models.DateTimeField('modificado', auto_now=True)

    class Meta:
        abstract = True


class Pais(TimeStampedModel):
    descripcion = models.CharField('Pais', max_length=100, blank=True, default='')

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        db_table = 'pais'

    def __str__(self):
        return f'{self.descripcion}'


class Proveedor(Persona):
    nombreProv = models.CharField('Nombre Proveedor', max_length=100, blank=True, default='')
    apellidoProv = models.CharField('Apellido Proveedor', max_length=100, blank=True, default='')
    emailProv = models.CharField('Email Proveedor', max_length=100, blank=True, default='')
    telefonoProv = models.CharField('Telefono Proveedor', max_length=100, blank=True, default='')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'

    def __str__(self):
        return f'{self.nombreEmp} - {self.nombreProv}'


class Cliente(Persona):
    nombreCli = models.CharField('Nombre Cliente', max_length=100, blank=True, default='')
    apellidoCli = models.CharField('Apellido Cliente', max_length=100, blank=True, default='')
    emailCli = models.CharField('Email Cliente', max_length=100, blank=True, default='')
    telefonoCli = models.CharField('Telefono Cliente', max_length=100, blank=True, default='')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'

    def __str__(self):
        return f'{self.nombreEmp} - {self.nombreCli}'
