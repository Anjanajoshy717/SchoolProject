from rest_framework import serializers
from .models import Subject, Section, Syllabus,SyllabusPart



class SyllabusPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyllabusPart
        fields = ['id','part_id', 'heading', 'description', 'image', 'video_url']


class SyllabusSerializer(serializers.ModelSerializer):
    section_title = serializers.CharField(source='section.title', read_only=True, allow_null=True)
    subject_name = serializers.CharField(source='section.subject.name', read_only=True, allow_null=True)
    class_name = serializers.SerializerMethodField(read_only=True)
    division = serializers.SerializerMethodField(read_only=True)
    parts = SyllabusPartSerializer(many=True, read_only=True)


    class Meta:
        model = Syllabus
        fields = ['syllabus_id', 'chapter_title', 'description', 'image', 'class_name', 'division', 'subject_name', 'section_title','parts']

    def get_class_name(self, obj):
        if obj.section and obj.section.subject:
            return f"Class {obj.section.subject.class_id}"
        return None

    def get_division(self, obj):
        if obj.section and obj.section.subject:
            class_id = obj.section.subject.class_id
            return "LP" if 1 <= class_id <= 4 else "HS"
        return None

    def validate(self, data):
        if self.context['request'].method == 'POST':
            syllabus_id = data.get("syllabus_id")
            if syllabus_id is None:
                raise serializers.ValidationError({"syllabus_id": "Syllabus ID is required for creating a syllabus."})
            if syllabus_id < 1:
                raise serializers.ValidationError({"syllabus_id": "Syllabus ID must be positive."})
        return data


class SectionSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True, allow_null=True)
    class_name = serializers.SerializerMethodField(read_only=True)
    division = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Section
        fields = ['unit_id', 'title', 'content', 'image', 'class_name', 'division', 'subject_name', ]

    def get_class_name(self, obj):
        if obj.subject:
            return f"Class {obj.subject.class_id}"
        return None

    def get_division(self, obj):
        if obj.subject:
            class_id = obj.subject.class_id
            return "LP" if 1 <= class_id <= 4 else "HS"
        return None

    def validate(self, data):
        if self.context['request'].method == 'POST':
            unit_id = data.get("unit_id")
            if unit_id is None:
                raise serializers.ValidationError({"unit_id": "Unit ID is required for creating a section."})
            if unit_id < 1:
                raise serializers.ValidationError({"unit_id": "Unit ID must be positive."})
        return data


class SubjectSerializer(serializers.ModelSerializer):
    class_name = serializers.SerializerMethodField(read_only=True)
    division = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Subject
        fields = ['class_id', 'subject_id', 'name', 'description', 'image', 'class_name', 'division', ]

    def get_class_name(self, obj):
        return f"Class {obj.class_id}"

    def get_division(self, obj):
        return "LP" if 1 <= obj.class_id <= 4 else "HS"

    def validate(self, data):
        method = self.context['request'].method
        class_id = data.get("class_id")
        subject_id = data.get("subject_id")
        if method == 'POST':
            if class_id is None:
                raise serializers.ValidationError({"class_id": "Class ID is required for creating a subject."})
            if subject_id is None:
                raise serializers.ValidationError({"subject_id": "Subject ID is required for creating a subject."})
        if class_id is not None:
            if not 1 <= class_id <= 10:
                raise serializers.ValidationError({"class_id": "Class ID must be between 1 and 10."})
        if subject_id is not None:
            if subject_id < 1:
                raise serializers.ValidationError({"subject_id": "Subject ID must be positive."})
        return data

class StaticClassSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    division = serializers.CharField()
    name = serializers.CharField()


# class SchoolClassSerializer(serializers.ModelSerializer):
#     subjects = SubjectSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = SchoolClass
#         fields = "__all__"
#
#     def validate(self, data):
#         division = data.get("division")
#         order = data.get("order")
#
#         if division is None:
#             raise serializers.ValidationError({"division": "Division is required."})
#
#         if order is None:
#             raise serializers.ValidationError({"order": "Order is required."})
#
#         if order < 1 or order > 10:
#             raise serializers.ValidationError("Classes must be between 1 and 10.")
#
#         if division == "LP" and not (1 <= order <= 4):
#             raise serializers.ValidationError("LP School can only have classes 1–4.")
#
#         if division == "HS" and not (5 <= order <= 10):
#             raise serializers.ValidationError("High School can only have classes 5–10.")
#
#         data["name"] = f"Class {order}"
#
#         return data
