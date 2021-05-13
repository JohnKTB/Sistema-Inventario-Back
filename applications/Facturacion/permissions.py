from rest_framework import permissions


class VentaPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('user.view_venta')
        elif request.method == 'PUT':
            return request.user.has_perm('user.change_venta')
        elif request.method == 'POST':
            return request.user.has_perm('user.add_venta')
        elif request.method == 'DELETE':
            return request.user.has_perm('user.delete_venta')
        return False


class DetalleVentaPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('user.view_detventa')
        elif request.method == 'PUT':
            return request.user.has_perm('user.change_detventa')
        elif request.method == 'POST':
            return request.user.has_perm('user.add_detventa')
        elif request.method == 'DELETE':
            return request.user.has_perm('user.delete_detventa')
        return False
