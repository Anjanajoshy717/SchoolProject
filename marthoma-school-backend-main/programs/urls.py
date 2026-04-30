# In your events/urls.py

# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from .views import EventViewSet, EventImageViewSet # <-- Add EventImageViewSet here

# router = DefaultRouter()
# router.register(r'events', EventViewSet, basename='events')
# router.register(r'event-images', EventImageViewSet, basename='event-images') # <-- Add this line

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# DELETE /api/event-images/104/
# PATCH /api/events/{id}/
# urls.py
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = router.urls