from django.conf.urls.static import static
from django.urls import path

from Inventario import settings
from applications.Contactos.views import FiltrarPaisAPI, PaisListAPI, FiltrarClientexNombreAPI, \
    FiltrarProveedorxNombreAPI

app_name = "contacto_app"

urlpatterns = [
    #PAIS
    path('api/filtrar-pais/<pais>', FiltrarPaisAPI.as_view(), name='filtrar_pais'),
    path('api/paises/', PaisListAPI.as_view(), name='paises'),
    #CLIENTE
    path('api/filtrar-cliente-nombre/<cliente>', FiltrarClientexNombreAPI.as_view(), name='filtrar_cliente_nombre'),
    #PROVEEDR
    path('api/filtrar-proveedor-nombre/<proveedor>', FiltrarProveedorxNombreAPI.as_view(), name='filtrar_proveedor_nombre'),
] + static(settings.local.MEDIA_URL, document_root=settings.local.MEDIA_ROOT)
