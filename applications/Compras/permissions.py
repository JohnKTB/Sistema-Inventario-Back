from rest_framework import permissions


class FabricantePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('user.view_fabricante')
        elif request.method == 'PUT':
            return request.user.has_perm('user.change_fabricante')
        elif request.method == 'POST':
            return request.user.has_perm('user.add_fabricante')
        elif request.method == 'DELETE':
            return request.user.has_perm('user.delete_fabricante')
        return False


class ProductoPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('user.view_producto')
        elif request.method == 'PUT':
            return request.user.has_perm('user.change_producto')
        elif request.method == 'POST':
            return request.user.has_perm('user.add_producto')
        elif request.method == 'DELETE':
            return request.user.has_perm('user.delete_producto')
        return False
