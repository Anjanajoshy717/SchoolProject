from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SportEventViewSet, SportImageViewSet, WinnerViewSet

router = DefaultRouter()

# router.register('sports', SportEventViewSet)
# router.register('sports-images', SportImageViewSet)
# router.register('sports-winners', WinnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
