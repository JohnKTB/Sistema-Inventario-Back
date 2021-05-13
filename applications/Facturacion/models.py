from django.db import models
from model_utils.models import TimeStampedModel

from applications.Compras.models import Producto
from applications.Contactos.models import Cliente


"""En venta va lo que no se repite"""


class venta(TimeStampedModel):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    IGV = models.FloatField('IGV', default=0.18)
    precioT = models.DecimalField(
        'Precio Venta',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    created = models.DateTimeField('creado', auto_now_add=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'venta'

    def __str__(self):
        return f'{self.id}'


"""En venta detalle va lo que se repite"""


class detVenta(TimeStampedModel):
    venta = models.ForeignKey(venta,
                              on_delete=models.CASCADE,
                              null=True, related_name='venta_detVent'
                              )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    cantidad = models.PositiveIntegerField('Cantidad Producto', blank=True, default='')
    precioU = models.PositiveIntegerField('Precio Unitario', blank=True, default=0)
    precioT = models.PositiveIntegerField('Precio Total', blank=True, default=0)

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalle Ventas'
        db_table = 'detVent'

    def __str__(self):
        return f'{self.id} - {self.venta} - {self.cantidad} - {self.producto.nombre}'
