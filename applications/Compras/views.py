
from rest_framework.generics import ListAPIView

from applications.Compras.models import Fabricante, Producto
from applications.Compras.serializers import FabricanteListSerializer, ProdImagesSerializer, FabricanteDescSerializer, \
    ProductosListSerializers


class FiltrarFabricanteAPI(ListAPIView):
    serializer_class = FabricanteListSerializer

    def get_queryset(self):
        letras = self.kwargs['nombre']
        return Fabricante.objects.filter(descripcion__icontains=letras)[:10]


class FiltrarFabricanteActivoAPI(ListAPIView):
    serializer_class = FabricanteDescSerializer

    def get_queryset(self):
        fabricante = self.kwargs['fabricante']
        return Fabricante.objects.filter(descripcion__icontains=fabricante, estado=0)[:10]


class FiltrarProductoAPI(ListAPIView):
    serializer_class = ProductosListSerializers

    def get_queryset(self):
        producto = self.kwargs['producto']
        return Producto.objects.filter(nombre__icontains=producto)[:10]


class ListProdImagesView(ListAPIView):
    serializer_class = ProdImagesSerializer
    queryset = Producto.objects.all()
