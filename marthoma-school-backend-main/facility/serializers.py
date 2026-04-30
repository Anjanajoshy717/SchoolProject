from rest_framework import serializers
from .models import WeProvide,Facility

class WeProvideSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeProvide
        fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'
