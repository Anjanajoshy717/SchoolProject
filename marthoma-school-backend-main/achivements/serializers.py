from rest_framework import serializers
from .models import Achievements, AchievementImage

class AchievementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementImage
        fields = ['id', 'image']

class AchievementSerializer(serializers.ModelSerializer):
    images = AchievementImageSerializer(many=True, read_only=True)
    images_to_delete = serializers.ListField(
        child=serializers.IntegerField(), 
        write_only=True, 
        required=False
    )

    class Meta:
        model = Achievements
        fields = ['id', 'title', 'description', 'date', 'images', 'images_to_delete', 'created_at']