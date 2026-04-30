# from rest_framework import serializers
# from .models import Event, EventImage

# class EventImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EventImage
#         fields = ['id', 'image']

# class EventSerializer(serializers.ModelSerializer):
#     # This is the read-only field for displaying images in the response
#     images = EventImageSerializer(many=True, read_only=True)
#     images_to_delete = serializers.ListField(
#         child=serializers.IntegerField(), 
#         write_only=True, 
#         required=False
#      )
#     class Meta:
#         model = Event
#         fields = [
#             'id', 'title', 'description', 'location', 'event_date', 'time',
#             'category', 'organizer', 'status', 'created_at', 'images','images_to_delete'
#         ] 

# events/serializers.py
from rest_framework import serializers
from .models import Event, EventImage, Winner

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['id', 'image']
        extra_kwargs = {'id': {'read_only': False, 'required': False}}

class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = ['id', 'name', 'photo', 'student_class', 'position']
        extra_kwargs = {'id': {'read_only': False, 'required': False}}

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, required=False)
    winners = WinnerSerializer(many=True, required=False)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'location', 'event_date', 'time',
            'category', 'organizer', 'status', 'created_at', 'images', 'winners'
        ]
        read_only_fields = ['created_at']

    def create(self, validated_data):
        winners_data = validated_data.pop('winners', [])
        images_data = validated_data.pop('images', [])

        event = Event.objects.create(**validated_data)

        for winner_data in winners_data:
            Winner.objects.create(event=event, **winner_data)
        
        for image_data in images_data:
            EventImage.objects.create(event=event, **image_data)

        return event

    def update(self, instance, validated_data):
        winners_data = validated_data.pop('winners', [])
        images_data = validated_data.pop('images', [])

        # Update event fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update or create winners
        winner_ids_to_keep = []
        for winner_data in winners_data:
            winner_id = winner_data.get('id')
            if winner_id:
                Winner.objects.filter(id=winner_id, event=instance).update(**winner_data)
                winner_ids_to_keep.append(winner_id)
            else:
                new_winner = Winner.objects.create(event=instance, **winner_data)
                winner_ids_to_keep.append(new_winner.id)

        # Delete winners that were not in the updated list
        Winner.objects.filter(event=instance).exclude(id__in=winner_ids_to_keep).delete()

        # Update or create images
        image_ids_to_keep = []
        for image_data in images_data:
            image_id = image_data.get('id')
            if image_id:
                EventImage.objects.filter(id=image_id, event=instance).update(**image_data)
                image_ids_to_keep.append(image_id)
            else:
                new_image = EventImage.objects.create(event=instance, **image_data)
                image_ids_to_keep.append(new_image.id)
        
        # Delete images that were not in the updated list
        EventImage.objects.filter(event=instance).exclude(id__in=image_ids_to_keep).delete()

        return instance