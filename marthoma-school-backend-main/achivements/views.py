from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Achievements, AchievementImage
from .serializers import AchievementSerializer
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievements.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        images_data = request.FILES.getlist('images')
        
        achievement_serializer = self.get_serializer(data=request.data)
        achievement_serializer.is_valid(raise_exception=True)
        achievement = achievement_serializer.save()

        for image_file in images_data:
            AchievementImage.objects.create(achievement=achievement, image=image_file)

        headers = self.get_success_headers(achievement_serializer.data)
        return Response(achievement_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object() 
        images_to_add = request.FILES.getlist('images', [])
        images_to_delete_ids = request.data.get('images_to_delete', [])

        # Update the achievement's text fields
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Delete specified images
        if images_to_delete_ids:
            AchievementImage.objects.filter(id__in=images_to_delete_ids, achievement=instance).delete()
        
        # Add new images
        for image_file in images_to_add:
            AchievementImage.objects.create(achievement=instance, image=image_file)

        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
# In views.py

# ... (rest of your imports and views) ...

from rest_framework import viewsets
from .models import AchievementImage
from .serializers import AchievementImageSerializer
from .permissions import IsAdminOrReadOnly # or a more specific permission

class AchievementImageViewSet(viewsets.ModelViewSet):
    queryset = AchievementImage.objects.all()
    serializer_class = AchievementImageSerializer
    permission_classes = [IsAdminOrReadOnly]