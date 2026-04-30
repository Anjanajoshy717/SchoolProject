from rest_framework import generics
from django.shortcuts import render
from .models import WeProvide, Facility
from .serializers import WeProvideSerializer, FacilitySerializer



# WeProvide CRUD 
class WeProvideListCreateAPIView(generics.ListCreateAPIView):
    queryset = WeProvide.objects.all()
    serializer_class = WeProvideSerializer

class WeProvideRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeProvide.objects.all()
    serializer_class = WeProvideSerializer

#  Facility CRUD 
class FacilityListCreateAPIView(generics.ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class FacilityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
