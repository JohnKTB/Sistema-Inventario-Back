from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('user.view_user')
        elif request.method == 'PUT':
            return request.user.has_perm('user.change_user')
        elif request.method == 'POST':
            return request.user.has_perm('user.add_user')
        elif request.method == 'DELETE':
            return request.user.has_perm('user.delete_user')
        return False


class GruposPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('user.view_group')
        elif request.method == 'PUT':
            return request.user.has_perm('user.change_group')
        elif request.method == 'POST':
            return request.user.has_perm('user.add_group')
        elif request.method == 'DELETE':
            return request.user.has_perm('user.delete_group')
        return False
