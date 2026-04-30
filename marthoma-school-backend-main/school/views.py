from rest_framework import viewsets
from .models import SchoolPhoto
from .serializers import SchoolPhotoSerializer

class SchoolPhotoViewSet(viewsets.ModelViewSet):
    queryset = SchoolPhoto.objects.all()
    serializer_class = SchoolPhotoSerializer