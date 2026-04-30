from django.urls import path
from . import views

urlpatterns = [

    # WeProvide API
    path('api/weprovide/', views.WeProvideListCreateAPIView.as_view(), name='weprovide_list_create'),
    path('api/weprovide/<int:pk>/', views.WeProvideRetrieveUpdateDestroyAPIView.as_view(), name='weprovide_detail'),

    # Facility API
    path('api/facility/', views.FacilityListCreateAPIView.as_view(), name='facility_list_create'),
    path('api/facility/<int:pk>/', views.FacilityRetrieveUpdateDestroyAPIView.as_view(), name='facility_detail'),
]
