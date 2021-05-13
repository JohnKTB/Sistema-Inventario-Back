from rest_framework.routers import DefaultRouter

from applications.Compras.viewsets import FabricanteViewSets, ProductoViewSet

router = DefaultRouter()

router.register(r'fabricantes', FabricanteViewSets, basename='Fabricantes')
router.register(r'productos', ProductoViewSet, basename='Productos')

urlpatterns = router.urls
