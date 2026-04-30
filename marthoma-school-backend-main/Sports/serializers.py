from rest_framework import serializers
from .models import SportEvent, SportImage, Winner

class SportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportImage
        fields = ['id', 'event', 'image']


class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = ['id', 'event', 'name', 'photo', 'student_class', 'position']


class SportEventSerializer(serializers.ModelSerializer):
    images = SportImageSerializer(many=True, read_only=True)
    winners = WinnerSerializer(many=True, read_only=True)

    class Meta:
        model = SportEvent
        fields = ['id', 'title', 'description', 'created_at', 'images', 'winners']
