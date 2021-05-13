from rest_framework import serializers, pagination

from applications.Contactos.models import Cliente, Pais, Proveedor

"""PAIS"""


class PaisDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = (
            'id',
            'descripcion'
        )


"""CLIENTES"""


class ClientesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'


class ClientesListSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Cliente
        fields = (
            'id',
            'numeroImp',
            'nombreEmp',
            'telefonoEmp',
            'sitioWeb',
            'nombreCli',
            'telefonoCli',
            'emailCli',
            'direccion',
            'created'
        )


class ClientesCreateSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Cliente
        fields = (
            'id',
            'numeroImp',
            'nombreEmp',
            'telefonoEmp',
            'sitioWeb',
            'nombreCli',
            'apellidoCli',
            'telefonoCli',
            'emailCli',
            'direccion',
            'ciudad',
            'regionProvincia',
            'codPostal',
            'pais',
            'created'
        )


class ClientesUpdateSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Cliente
        fields = (
            'id',
            'numeroImp',
            'nombreEmp',
            'telefonoEmp',
            'sitioWeb',
            'nombreCli',
            'apellidoCli',
            'telefonoCli',
            'emailCli',
            'direccion',
            'ciudad',
            'regionProvincia',
            'codPostal',
            'pais',
            'created'
        )


class CLienteDetailSerializers(serializers.ModelSerializer):
    pais = PaisDescSerializer()

    class Meta:
        model = Cliente
        fields = (
            'id',
            'numeroImp',
            'nombreEmp',
            'telefonoEmp',
            'sitioWeb',
            'nombreCli',
            'apellidoCli',
            'telefonoCli',
            'emailCli',
            'direccion',
            'ciudad',
            'regionProvincia',
            'codPostal',
            'pais'
        )


"""PROVEEDOR"""


class ProveedoresSerializers(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = '__all__'


class ProveedoresListSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Proveedor
        fields = (
            'id',
            'numeroImp',
            'nombreEmp',
            'telefonoEmp',
            'sitioWeb',
            'nombreProv',
            'telefonoProv',
            'emailProv',
            'direccion',
            'created'
        )


class ProveedoresCreateSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Proveedor
        fields = (
            'id',
            'numeroImp',
            'nombreEmp',
            'telefonoEmp',
            'sitioWeb',
            'nombreProv',
            'apellidoProv',
            'telefonoProv',
            'emailProv',
            'direccion',
            'ciudad',
            'regionProvincia',
            'codPostal',
            'pais',
            'created'
        )


class ProveedorDetailSerializers(serializers.ModelSerializer):
    pais = PaisDescSerializer()

    class Meta:
        model = Proveedor
        fields = (
            'id',
            'numeroImp',
            'nombreEmp',
            'telefonoEmp',
            'sitioWeb',
            'nombreProv',
            'apellidoProv',
            'telefonoProv',
            'emailProv',
            'direccion',
            'ciudad',
            'regionProvincia',
            'codPostal',
            'pais'
        )


class ContactosPagination(pagination.PageNumberPagination):
    page_size = 10
