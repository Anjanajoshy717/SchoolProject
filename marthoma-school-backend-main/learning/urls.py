from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, SectionViewSet, SyllabusViewSet, StaticClassListAPIView,SyllabusPartViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'sections', SectionViewSet, basename='sections')
router.register(r'syllabus', SyllabusViewSet, basename='syllabus')
router.register(r'syllabus-parts', SyllabusPartViewSet, basename='syllabus-parts')


urlpatterns = [
    path('classes/', StaticClassListAPIView.as_view(), name='static-classes'),
    path('', include(router.urls)),
]