from rest_framework import viewsets, exceptions
from rest_framework.response import Response

from applications.Compras.models import Producto
from applications.Contactos.models import Cliente
from applications.Facturacion.models import venta, detVenta
from applications.Facturacion.permissions import VentaPermission, DetalleVentaPermission
from applications.Facturacion.serializers import ProcesoVentaSerializer, detVentaListSerializer, \
    detVentaPagination

"""NUEVA VENTA"""


class VentasViewSet(viewsets.ViewSet):
    querysets = venta.objects.all()
    permission_classes = (VentaPermission,)

    def permission_denied(self, request, message=None, code=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos!')

    def create(self, request, *args, **kwargs):
        serializer = ProcesoVentaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cliente = Cliente.objects.get(id=serializer.validated_data['cliente'])

        Venta = venta.objects.create(
            cliente=cliente,
            IGV=0.18,
            precioT=serializer.validated_data['precioTotal'],
        )

        # Los id de los productos llegan sin un orden, aqui django los ordena
        # por defecto, lo que descuadra con las cantidades
        productos = Producto.objects.filter(
            id__in=serializer.validated_data['productos']
        )

        cantidades = serializer.validated_data['cantidades']

        # Juntamos los productos y cantidades recibidos
        ProCant = []
        for prod, cant in zip(serializer.validated_data['productos'], cantidades):
            ProCant.append({'prod': prod, 'cant': cant})
        ventas_detalle = []

        # Solucion al problema de los id de productos ordenados por defecto
        for producto, cantidad in zip(productos, cantidades):
            for prod in ProCant:
                if producto.id == prod['prod']:
                    venta_detalle = detVenta(venta=Venta,
                                             producto=producto,
                                             cantidad=prod['cant'],
                                             precioU=producto.precioVenta,
                                             precioT=producto.precioVenta * prod['cant']
                                             )
            ventas_detalle.append(venta_detalle)

            producto.stockIn -= cantidad

        # '['stockIn']' aqui van los campos a actualizar
        Producto.objects.bulk_update(productos, ['stockIn'])
        detVenta.objects.bulk_create(ventas_detalle)

        return Response({
            'msj': 'venta exitosa'
        })


"""DETALLE DE VENTA"""


class detVentaViewSet(viewsets.ModelViewSet):
    serializer_class = detVentaListSerializer
    queryset = detVenta.objects.all().order_by('id')
    pagination_class = detVentaPagination
    permission_classes = (DetalleVentaPermission,)

    def permission_denied(self, request, message=None, code=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos!')

    def list(self, request, *args, **kwargs):
        queryset = detVenta.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = detVentaListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = detVentaListSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'msj': 'Factura Eliminada!'
        })
