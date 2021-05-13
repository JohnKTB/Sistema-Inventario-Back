from rest_framework import pagination, serializers

from Inventario.settings.local import MEDIA_URL
from applications.Compras.models import Fabricante, Producto

"""FABRICANTE"""


class FabricanteDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = (
            'id',
            'descripcion'
        )


class FabricanteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = (
            'id',
            'descripcion',
            'estado',
        )


class FabricanteListSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Fabricante
        fields = (
            'id',
            'descripcion',
            'estado',
            'created'
        )


class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = '__all__'


class FabricanteCreateSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    estado = serializers.IntegerField(read_only=True)

    class Meta:
        model = Fabricante
        fields = (
            'id',
            'descripcion',
            'estado',
            'created'
        )


"""PRODUCTOS"""


class ProdImagesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ('image_url',)

    def get_image_url(self, obj):
        return obj.imagen.url


class ProductosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductosListSerializers(serializers.ModelSerializer):
    fabricante = FabricanteDescSerializer()
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre',
            'imagen',
            'modelo',
            'estado',
            'stockIn',
            'precioVenta',
            'fabricante'
        )

    def get_imagen(self, instance):
        imagen = f'http://127.0.0.1:8000{MEDIA_URL}{instance.imagen}'
        return imagen


class ProductosDetailSerializers(serializers.ModelSerializer):
    fabricante = FabricanteDescSerializer()
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre',
            'modelo',
            'presentacion',
            'descripcion',
            'fabricante',
            'estado',
            'costo',
            'utilidad',
            'precioVenta',
            'stockIn',
            'imagen'
        )

    def get_imagen(self, instance):
        imagen = f'http://127.0.0.1:8000{MEDIA_URL}{instance.imagen}'
        return imagen


class ComprasPagination(pagination.PageNumberPagination):
    page_size = 10
