from django.contrib import admin

from applications.Contactos.models import Pais, Cliente, Proveedor

admin.site.register(Pais)
admin.site.register(Cliente)
admin.site.register(Proveedor)
