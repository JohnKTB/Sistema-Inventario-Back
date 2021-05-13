from rest_framework.routers import DefaultRouter

from applications.users.viewsets import GruposViewSet, PermisosViewSet, UsersViewSet

router = DefaultRouter()

router.register(r'usuarios', UsersViewSet, basename='usuarios')
router.register(r'grupos', GruposViewSet, basename='grupos')
router.register(r'permisos', PermisosViewSet, basename='permisos')

urlpatterns = router.urls
