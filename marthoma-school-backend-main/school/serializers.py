from rest_framework import serializers
from .models import SchoolPhoto

class SchoolPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolPhoto
        fields = ['id', 'title', 'image']