from rest_framework import permissions

class IsAdminOrSubadminOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - SAFE_METHODS (GET, HEAD, OPTIONS) are allowed for everyone
    - Write permissions (POST, PUT, PATCH, DELETE) are only allowed
      to users who are:
        - Admins (is_staff=True)
        - OR members of the 'subadmin' group
    """
    
    def has_permission(self, request, view):
        # Allow read-only methods for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write methods only for admin or subadmin
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.is_staff  # Admin check
                or request.user.groups.filter(name='subadmin').exists()  # Subadmin group check
            )
        )
