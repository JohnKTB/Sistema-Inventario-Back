from django.urls import path

from applications.users.views import FiltrarUsuarioxNombreAPI, UsuarioAPI

app_name = "usuario_app"

urlpatterns = [
    path('api/filtrar-usuario/<usuario>', FiltrarUsuarioxNombreAPI.as_view(), name='filtrar_usuario'),
    path('api/usuario-logeado/', UsuarioAPI.as_view(), name='usuario_logeado'),
]
