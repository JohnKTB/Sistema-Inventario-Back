from django.contrib.auth.models import Group, Permission
from rest_framework import viewsets, status, exceptions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from applications.users.models import User
from applications.users.permissions import UserPermission, GruposPermission
from applications.users.serializers import GruposSerializer, PermisosSerializer, GruposCreateSerializer, \
    PermisosIdsSerializer, createUserSerializer, UsuarioDetailSerializer, \
    UserUpdateSerializer, UsuariosListSerializer


# USUARIOS


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all().order_by('id')
    permission_classes = (UserPermission,)

    def permission_denied(self, request, message=None, code=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos!')

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all().order_by('id')
        serializer = UsuariosListSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = createUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        nombres = serializer.validated_data['Nombres']
        apePat = serializer.validated_data['ApePat']
        apeMat = serializer.validated_data['ApeMat']
        user = User.objects.create(
            username=serializer.validated_data['username'],
            Nombres=serializer.validated_data['Nombres'],
            ApePat=serializer.validated_data['ApePat'],
            ApeMat=serializer.validated_data['ApeMat'],
            NombreCompleto=nombres + ' ' + apePat + ' ' + apeMat,
            is_staff=False,
            is_superuser=False,
            is_active=True,
            email=serializer.validated_data['email'],
        )
        user.groups.set(serializer.validated_data['groups'])
        user.set_password(serializer.validated_data['password'])
        user.save()
        serializerss = UsuariosListSerializer(user)

        return Response(serializerss.data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        Nombres = serializer.context['request'].data['Nombres']
        ApePat = serializer.context['request'].data['ApePat']
        ApeMat = serializer.context['request'].data['ApeMat']
        serializer.save(NombreCompleto=Nombres + ' ' + ApePat + ' ' + ApeMat)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'msj': 'Usuario Eliminado!'
        })

    def retrieve(self, request, pk=None):
        userDetail = get_object_or_404(User.objects.all(), pk=pk)
        # Deserializamos
        serializer = UsuarioDetailSerializer(userDetail)
        return Response(serializer.data)

# GRUPOS


class GruposViewSet(viewsets.ModelViewSet):
    serializer_class = GruposSerializer
    queryset = Group.objects.all().order_by('id')
    permission_classes = (GruposPermission,)

    def permission_denied(self, request, message=None, code=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos!')

    def create(self, request, *args, **kwargs):
        serializer = GruposCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        grupo = Group(name=serializer.validated_data['rol'])
        grupo.save()
        permisos = []
        for permiso in serializer.validated_data['permisos']:
            query = Permission.objects.filter(name__icontains=permiso)
            for permId in PermisosIdsSerializer(query, many=True).data:
                permisos.append(permId['id'])
        permisosAgregar = Permission.objects.filter(
            id__in=permisos
        )
        grupo.permissions.set(permisosAgregar)
        return Response({
            'msj': 'Grupo Creado!'
        })

    def update(self, request, *args, **kwargs):

        serializer = GruposCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        Group.objects.filter(id=self.kwargs['pk']).update(name=serializer.validated_data['rol'])

        grupo = Group.objects.get(id=self.kwargs['pk'])

        permisos = []
        for permiso in serializer.validated_data['permisos']:
            query = Permission.objects.filter(name__icontains=permiso)
            for permId in PermisosIdsSerializer(query, many=True).data:
                permisos.append(permId['id'])
        permisosAgregar = Permission.objects.filter(
            id__in=permisos
        )
        grupo.permissions.set(permisosAgregar)

        return Response({'msj': 'Rol Actualizado'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'msj': 'Rol Eliminado!'
        })


class PermisosViewSet(viewsets.ModelViewSet):
    serializer_class = PermisosSerializer
    queryset = Permission.objects.exclude(content_type__in=[1, 2, 4, 5])
