from rest_framework.routers import DefaultRouter
from .views import AchievementViewSet,AchievementImageViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'achievements', AchievementViewSet, basename='achievements')  # base '' because main prefix handles /achievements/
router.register(r'achievement-images', AchievementImageViewSet) # Add this line
urlpatterns = [
    path('', include(router.urls)),
]

