from django.db import models
from model_utils.models import TimeStampedModel


class Fabricante(TimeStampedModel):
    descripcion = models.CharField('Fabricante', max_length=100, blank=True, default='')
    estado = models.PositiveSmallIntegerField('Estado Fabricante', null=True, default=0)
    created = models.DateTimeField('creado', auto_now_add=True)
    modified = models.DateTimeField('modificado', auto_now=True)

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'
        db_table = 'fabricante'

    def __str__(self):
        return f'{self.descripcion} - {self.estado}'


class Producto(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=100, blank=True, default='')
    modelo = models.CharField('Modelo', max_length=100, blank=True, default='')
    presentacion = models.CharField('Presentacion', max_length=100, blank=True, default='')
    descripcion = models.CharField('Descripcion', max_length=100, blank=True, default='')
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, null=True)
    estado = models.PositiveSmallIntegerField('Estado Producto', null=True, default=0)
    costo = models.FloatField('Costo', null=True)
    utilidad = models.FloatField('Utilidad', null=True)
    precioVenta = models.FloatField('Precio de Venta', null=True)
    stockIn = models.IntegerField('Stock Inicial', null=True)
    imagen = models.ImageField('Imagen Producto', blank=True, null=True, upload_to='productos')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.precioVenta} - {self.stockIn}'
