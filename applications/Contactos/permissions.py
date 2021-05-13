from rest_framework import permissions


class ClientePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('user.view_cliente')
        elif request.method == 'PUT':
            return request.user.has_perm('user.change_cliente')
        elif request.method == 'POST':
            return request.user.has_perm('user.add_cliente')
        elif request.method == 'DELETE':
            return request.user.has_perm('user.delete_cliente')
        return False


class ProveedorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('user.view_proveedor')
        elif request.method == 'PUT':
            return request.user.has_perm('user.change_proveedor')
        elif request.method == 'POST':
            return request.user.has_perm('user.add_proveedor')
        elif request.method == 'DELETE':
            return request.user.has_perm('user.delete_proveedor')
        return False
