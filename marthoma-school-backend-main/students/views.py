# students/views.py
from rest_framework import permissions

class CustomStudentPermission(permissions.BasePermission):
    """
    Custom permission for student management.
    - Admins and Sub-admins have full permissions (GET, POST, PUT, PATCH, DELETE).
    - Students have read-only permissions (GET, HEAD, OPTIONS).
    """

    def has_permission(self, request, view):
        # A user must be authenticated to access this view.
        if not request.user or not request.user.is_authenticated:
            return False

        # Admins and Sub-admins have full access.
        if request.user.role in ['admin', 'subadmin']:
            return True

        # Students and other users only have read-only access (safe methods).
        if request.user.role == 'student':
            return request.method in permissions.SAFE_METHODS

        # For any other roles not explicitly defined, deny access.
        return False
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Q  
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [CustomStudentPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['student_class', 'section', 'gender', 'date_of_birth']
    search_fields = ['user__first_name', 'user__last_name']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)

        if search_query:
            # Split the search query into potential first and last names
            parts = search_query.split()
            first_name = parts[0] if len(parts) > 0 else ''
            last_name = parts[1] if len(parts) > 1 else ''

            # Create a Q object for the search
            # This logic will find matches where the full search query
            # matches either first name OR last name OR a combination
            query = Q(user__first_name__icontains=first_name) | Q(user__last_name__icontains=last_name)

            if len(parts) > 1:
                # Add a specific condition for a two-part search
                # This ensures "John Doe" matches first name John and last name Doe
                query |= Q(user__first_name__icontains=first_name, user__last_name__icontains=last_name)

            queryset = queryset.filter(query)

        return queryset