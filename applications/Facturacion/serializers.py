from rest_framework import serializers, pagination

from applications.Compras.models import Producto
from applications.Contactos.models import Cliente
from applications.Facturacion.models import venta, detVenta

"""VENTA"""


class ClientesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = (
            'nombreCli',
            'apellidoCli'
        )


class VentaListSerializer(serializers.ModelSerializer):
    cliente = ClientesSerializers()

    class Meta:
        model = venta
        fields = (
            'id',
            'cliente',
        )


"""VENTA DETALLE"""


class detVentaListSerializer(serializers.ModelSerializer):
    venta = VentaListSerializer()

    class Meta:
        model = detVenta
        fields = (
            'id',
            'precioT',
            'cantidad',
            'venta',
        )


class ProductosListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = (
            'nombre',
        )


class VentaListPDFSerializer(serializers.ModelSerializer):

    class Meta:
        model = venta
        fields = (
            'precioT',
        )


class detVentaListPDFSerializer(serializers.ModelSerializer):
    producto = ProductosListSerializers()
    venta = VentaListPDFSerializer()

    class Meta:
        model = detVenta
        fields = (
            'cantidad',
            'precioU',
            'precioT',
            'producto',
            'venta'
        )


class ArrayIntegerSerializer(serializers.ListField):
    child = serializers.IntegerField()


class ProcesoVentaSerializer(serializers.Serializer):
    cliente = serializers.IntegerField()
    productos = ArrayIntegerSerializer()
    cantidades = ArrayIntegerSerializer()
    precioTotal = serializers.FloatField()


class detVentaPagination(pagination.PageNumberPagination):
    page_size = 10
