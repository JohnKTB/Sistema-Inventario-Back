from django.contrib import admin

from applications.Facturacion.models import venta, detVenta

admin.site.register(venta)
admin.site.register(detVenta)
