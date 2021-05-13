from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Usuarios
from applications.users.models import User


class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = '__all__'


class GrupoNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'name',
        )


class UsuariosListSerializer(serializers.ModelSerializer):
    groups = GrupoNameSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'NombreCompleto',
            'username',
            'groups',
            'email'
        )


class PermisosRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = (
            'codename',
        )


class GruposSerializer(serializers.ModelSerializer):
    permissions = PermisosRolSerializer(many=True)

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'permissions'
        )


class RolUsuarioLogeadoSerializer(serializers.ModelSerializer):
    groups = GruposSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'username',
            'groups',
        )


class createUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'Nombres',
            'ApePat',
            'ApeMat',
            'username',
            'password',
            'groups',
            'email',
        )
        extra_kwargs = {'password': {'write_only': True}}


class UsuarioDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'Nombres',
            'ApePat',
            'ApeMat',
            'username',
            'groups',
            'email'
        )


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'NombreCompleto',
            'Nombres',
            'ApePat',
            'ApeMat',
            'username',
            'groups',
            'email'
        )

# GRUPOS


class PermisosNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = (
            'name',
        )


class GruposSerializer(serializers.ModelSerializer):
    permissions = PermisosNameSerializer(many=True)

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'permissions'
        )


class ArrayStringsSerializer(serializers.ListField):
    child = serializers.CharField()


class GruposCreateSerializer(serializers.Serializer):
    rol = serializers.CharField()
    permisos = ArrayStringsSerializer()


# PERMISOS


class PermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = (
            'id',
            'name',
            'codename',
            'content_type'
        )


class PermisosIdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = (
            'id',
        )


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def get_token(self, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...
        return token
