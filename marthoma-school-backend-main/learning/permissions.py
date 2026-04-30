# from rest_framework import permissions

# class IsAdminOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user and request.user.is_staff


# events/permissions.py

from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to read events
    and only staff/superusers to edit them.
    """
    def has_permission(self, request, view):
        # Allow read-only access for all authenticated users
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        # Allow write access for staff and superusers
        return request.user and (request.user.is_staff or request.user.is_superuser)

from rest_framework import permissions

# class IsAdminOrSubAdmin(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Allow read-only access (GET, HEAD, OPTIONS) only for authenticated users
#         if request.method in permissions.SAFE_METHODS:
#             return request.user and request.user.is_authenticated
        
#         # Allow full access (POST, PUT, PATCH, DELETE) only for staff and superusers
#         return request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff)
class IsAdminOrSubAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access (GET, HEAD, OPTIONS) for any authenticated user.
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Allow full access (POST, PUT, PATCH, DELETE) only for 'admin' and 'subadmin' roles.
        return request.user and request.user.is_authenticated and (request.user.role in ['admin', 'subadmin'])