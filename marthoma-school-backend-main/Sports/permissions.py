from rest_framework import permissions

class IsAdminOrSubAdmin(permissions.BasePermission):
        def has_permission(self, request, view):
            if request.method in permissions.SAFE_METHODS:  # allows GET, HEAD, OPTIONS
                return True
            return request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff)


