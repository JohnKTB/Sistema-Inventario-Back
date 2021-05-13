
from rest_framework.generics import ListAPIView

from applications.Contactos.models import Pais, Cliente, Proveedor
from applications.Contactos.serializers import PaisDescSerializer, ClientesListSerializers, ProveedoresListSerializers

"""PAIS"""


class PaisListAPI(ListAPIView):
    queryset = Pais.objects.all()[:10]
    serializer_class = PaisDescSerializer


class FiltrarPaisAPI(ListAPIView):
    serializer_class = PaisDescSerializer

    def get_queryset(self):
        pais = self.kwargs['pais']
        return Pais.objects.filter(descripcion__icontains=pais)[:10]


"""CLIENTE"""


class FiltrarClientexNombreAPI(ListAPIView):
    serializer_class = ClientesListSerializers

    def get_queryset(self):
        cliente = self.kwargs['cliente']
        return Cliente.objects.filter(nombreCli__icontains=cliente)[:10]


"""PROVEEDOR"""


class FiltrarProveedorxNombreAPI(ListAPIView):
    serializer_class = ProveedoresListSerializers

    def get_queryset(self):
        proveedor = self.kwargs['proveedor']
        return Proveedor.objects.filter(nombreProv__icontains=proveedor)[:10]
