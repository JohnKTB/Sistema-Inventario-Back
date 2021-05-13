from django.urls import path

from applications.Facturacion.views import testeando, PDF

app_name = "factura_app"

urlpatterns = [
    path('api/pdf/', PDF.as_view(), name='test'),
]
