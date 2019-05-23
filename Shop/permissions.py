from rest_framework import permissions

class IsCustomer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user

class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user