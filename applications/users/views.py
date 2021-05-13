from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from applications.users.models import User
from applications.users.serializers import MyTokenObtainPairSerializer, UsuariosListSerializer, \
    RolUsuarioLogeadoSerializer


class FiltrarUsuarioxNombreAPI(ListAPIView):
    serializer_class = UsuariosListSerializer

    def get_queryset(self):
        usuario = self.kwargs['usuario']
        return User.objects.filter(NombreCompleto__icontains=usuario)[:10]


class UsuarioAPI(ListAPIView):
    serializer_class = RolUsuarioLogeadoSerializer

    def list(self, request, *args, **kwargs):

        queryset = User.objects.filter(username__icontains=self.request.user)
        serializer = RolUsuarioLogeadoSerializer(queryset, many=True)

        return Response(serializer.data)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
