import os.path
from os import path

from rest_framework import viewsets, status, exceptions
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response

from applications.Compras.models import Fabricante, Producto
from applications.Compras.permissions import FabricantePermission, ProductoPermission
from applications.Compras.serializers import FabricanteSerializer, ComprasPagination, FabricanteListSerializer, \
    FabricanteDetailSerializer, FabricanteCreateSerializer, ProductosSerializers, ProductosListSerializers, \
    ProductosDetailSerializers

"""FABRICANTES"""


class FabricanteViewSets(viewsets.ModelViewSet):
    serializer_class = FabricanteSerializer
    queryset = Fabricante.objects.all().order_by('id')
    pagination_class = ComprasPagination
    permission_classes = (FabricantePermission,)

    def permission_denied(self, request, message=None, code=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos!')

    def list(self, request, *args, **kwargs):
        queryset = Fabricante.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = FabricanteListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = FabricanteListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = FabricanteCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({'msj': 'Fabricante Actualizado!'})

    def retrieve(self, request, pk=None):
        citaDetail = get_object_or_404(Fabricante.objects.all(), pk=pk)
        # Deserializamos
        serializer = FabricanteDetailSerializer(citaDetail)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'msj': 'Fabricante Eliminado'
        })


"""PRODUCTOS"""


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductosSerializers
    queryset = Producto.objects.all().order_by('id')
    pagination_class = ComprasPagination
    parser_classes = (MultiPartParser, FileUploadParser)
    permission_classes = (ProductoPermission,)

    def permission_denied(self, request, message=None, code=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos!')

    def list(self, request, *args, **kwargs):
        queryset = Producto.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProductosListSerializers(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ProductosListSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print(self.request.data)
        productoDetail = get_object_or_404(Producto.objects.all(), pk=pk)
        # Deserializamos
        serializer = ProductosDetailSerializers(productoDetail)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'msj': 'Producto Eliminado!'
        })
