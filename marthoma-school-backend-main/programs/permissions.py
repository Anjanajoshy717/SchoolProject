# from rest_framework import permissions

# class IsAdminOrSubAdmin(permissions.BasePermission):
#         def has_permission(self, request, view):
#             if request.method in permissions.SAFE_METHODS:  # allows GET, HEAD, OPTIONS
#                 return True
#             return request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff)
from rest_framework import permissions

class IsAdminOrSubAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access (GET, HEAD, OPTIONS) for any authenticated user.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow full access (POST, PUT, PATCH, DELETE) only for 'admin' and 'subadmin' roles.
        return request.user and request.user.is_authenticated and (request.user.role in ['admin', 'subadmin'])