from rest_framework.routers import DefaultRouter

from applications.Contactos.viewsets import ClienteViewSets, ProveedorViewSets

router = DefaultRouter()

router.register(r'clientes', ClienteViewSets, basename='clientes')
router.register(r'proveedores', ProveedorViewSets, basename='proveedores')

urlpatterns = router.urls
