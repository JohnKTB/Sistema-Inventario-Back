from django.contrib import admin

from applications.Compras.models import Fabricante, Producto

admin.site.register(Fabricante)
admin.site.register(Producto)
