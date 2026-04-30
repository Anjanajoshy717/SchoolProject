# students/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
# GET	/students/	List all student profiles.
# POST	/students/	Create a new student profile and user account.
# GET	/students/{id}/	Retrieve a single student's profile.
# PUT	/students/{id}/	Update a student's entire profile.
# PATCH	/students/{id}/	Partially Update a student's profile.
# DELETE	/students/{id}/	Delete a student's profile and user account.