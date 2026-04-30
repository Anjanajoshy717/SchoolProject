from rest_framework import serializers
from .models import SchoolReview

class SchoolReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SchoolReview
        fields = ['id', 'user', 'school_name', 'rating', 'comment', 'created_at']
