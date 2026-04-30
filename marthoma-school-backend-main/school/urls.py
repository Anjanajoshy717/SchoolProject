from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolPhotoViewSet

router = DefaultRouter()
router.register('school-photos', SchoolPhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]