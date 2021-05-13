from rest_framework.routers import DefaultRouter

from applications.Facturacion.viewsets import VentasViewSet, detVentaViewSet

router = DefaultRouter()

router.register(r'ventas', VentasViewSet, basename='ventas')
router.register(r'detalle-venta', detVentaViewSet, basename='detalle_venta')

urlpatterns = router.urls
