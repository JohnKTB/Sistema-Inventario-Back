from django.conf.urls.static import static
from django.urls import path

from Inventario import settings
from applications.Compras.views import FiltrarFabricanteAPI, FiltrarFabricanteActivoAPI, \
    FiltrarProductoAPI

app_name = "compras_app"

urlpatterns = [
    path('api/filtrar-fabricante/<nombre>', FiltrarFabricanteAPI.as_view(), name='filtrar_fabricante'),
    path('api/filtrar-fabricante-activo/<fabricante>', FiltrarFabricanteActivoAPI.as_view(), name='filtrar_fabricante_activo'),
    path('api/filtrar-producto/<producto>', FiltrarProductoAPI.as_view(), name='filtrar_producto'),

] + static(settings.local.MEDIA_URL, document_root=settings.local.MEDIA_ROOT)
