from rest_framework import viewsets, status, exceptions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from applications.Contactos.models import Cliente, Proveedor
from applications.Contactos.permissions import ClientePermission, ProveedorPermission
from applications.Contactos.serializers import ContactosPagination, ClientesListSerializers, ClientesCreateSerializers, \
    CLienteDetailSerializers, ClientesSerializers, ProveedoresSerializers, ProveedoresListSerializers, \
    ProveedorDetailSerializers, ProveedoresCreateSerializers, ClientesUpdateSerializers

"""CLIENTE"""


class ClienteViewSets(viewsets.ModelViewSet):
    serializer_class = ClientesSerializers
    queryset = Cliente.objects.all().order_by('id')
    pagination_class = ContactosPagination
    permission_classes = (ClientePermission,)

    def permission_denied(self, request, message=None, code=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos!')

    def list(self, request, *args, **kwargs):
        queryset = Cliente.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ClientesListSerializers(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ClientesListSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print(self.request.data)
        clienteDetail = get_object_or_404(Cliente.objects.all(), pk=pk)
        # Deserializamos
        serializer = CLienteDetailSerializers(clienteDetail)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ClientesCreateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ClientesUpdateSerializers(instance, data=request.data, partial=partial)
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
            'msj': 'Cliente Eliminado'
        })


"""PROOVEDOR"""


class ProveedorViewSets(viewsets.ModelViewSet):
    serializer_class = ProveedoresSerializers
    queryset = Proveedor.objects.all().order_by('id')
    pagination_class = ContactosPagination
    permission_classes = (ProveedorPermission,)

    def permission_denied(self, request, message=None, code=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos!')

    def list(self, request, *args, **kwargs):
        queryset = Proveedor.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProveedoresListSerializers(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ProveedoresListSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print(self.request.data)
        ProveedorDetail = get_object_or_404(Proveedor.objects.all(), pk=pk)
        # Deserializamos
        serializer = ProveedorDetailSerializers(ProveedorDetail)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ProveedoresCreateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'msj': 'Proveedor Eliminado'
        })