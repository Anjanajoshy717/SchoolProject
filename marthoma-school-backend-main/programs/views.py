
# from rest_framework import viewsets, permissions, status
# from rest_framework.response import Response
# from .models import Event, EventImage
# from .serializers import EventSerializer, EventImageSerializer

# class IsAdminOrSubAdmin(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user and (request.user.is_staff or request.user.is_superuser)

# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     permission_classes = [IsAdminOrSubAdmin]

#     def create(self, request, *args, **kwargs):
#         images_data = request.FILES.getlist('images')

#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         event = serializer.save()
    
#         for image_file in images_data:
#             EventImage.objects.create(event=event, image=image_file)

#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, *args, **kwargs):

#         instance = self.get_object()
#         images_to_add = request.FILES.getlist('images', [])
#         images_to_delete_ids = request.data.get('images_to_delete', [])

#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         # Delete specified images
#         if images_to_delete_ids:
#             EventImage.objects.filter(id__in=images_to_delete_ids, event=instance).delete()

#         # Add new images
#         for image_file in images_to_add:
#             EventImage.objects.create(event=instance, image=image_file)

#         return Response(serializer.data)
    
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class EventImageViewSet(viewsets.ModelViewSet):
#     queryset = EventImage.objects.all()
#     serializer_class = EventImageSerializer
#     permission_classes = [IsAdminOrSubAdmin]
# events/views.py
from rest_framework import viewsets, permissions, status
from .models import Event
from .serializers import EventSerializer
from .filters import EventFilter
from .permissions import IsAdminOrSubAdmin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Custom permission class (assuming it's already defined)
# class IsAdminOrSubAdmin(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user and (request.user.is_staff or request.user.is_superuser)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminOrSubAdmin]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_class = EventFilter
    # Specify which fields to use for searching
    search_fields = ['title', 'description', 'organizer', 'location', 'event_date']
