from django.urls import path
from .views import AdvertisementListCreateAPIView, AdvertisementDetailAPIView

urlpatterns = [
    path('ads/', AdvertisementListCreateAPIView.as_view(), name='ads-list-create'),
    path('ads/<int:pk>/', AdvertisementDetailAPIView.as_view(), name='ads-detail'),
]
