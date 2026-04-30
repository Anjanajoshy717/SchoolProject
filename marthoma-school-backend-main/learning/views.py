from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from .models import Subject, Section, Syllabus,SyllabusPart
from .serializers import (
    SubjectSerializer, SectionSerializer, SyllabusSerializer, StaticClassSerializer, SyllabusPartSerializer
)
from .permissions import IsAdminOrReadOnly,IsAdminOrSubAdmin

class StaticClassListAPIView(APIView):
    def get(self, request):
        classes = []
        for i in range(1, 5):
            classes.append({"class_id": i, "division": "LP", "name": f"Class {i}"})
        for i in range(5, 11):
            classes.append({"class_id": i, "division": "HS", "name": f"Class {i}"})
        serializer = StaticClassSerializer(classes, many=True)
        return Response(serializer.data)

class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminOrSubAdmin]
    lookup_field = 'subject_id'
    pagination_class = None
    def get_queryset(self):
        queryset = Subject.objects.all()
        class_id = self.request.query_params.get('class')
        if class_id:
            try:
                class_id = int(class_id)
                queryset = queryset.filter(class_id=class_id)
            except ValueError:
                raise ValidationError({"class": "Query parameter 'class' must be a valid integer."})
        return queryset

    def perform_create(self, serializer):
        class_id = self.request.query_params.get('class')
        if not class_id:
            raise ValidationError({"class": "Query parameter 'class' is required for creating a subject."})
        try:
            class_id = int(class_id)
            if not 1 <= class_id <= 10:
                raise ValueError
        except ValueError:
            raise ValidationError({"class": "Invalid class ID. Must be integer between 1 and 10."})
        try:
            serializer.save(class_id=class_id)
        except IntegrityError as e:
            if "unique constraint" in str(e) and "class_id_subject_id" in str(e):
                raise ValidationError({
                    "non_field_errors": [f"A subject with subject_id={serializer.validated_data['subject_id']} already exists for class_id={class_id}."]
                })
            raise

    def perform_update(self, serializer):
        try:
            serializer.save()
        except IntegrityError as e:
            if "unique constraint" in str(e) and "class_id_subject_id" in str(e):
                raise ValidationError({
                    "non_field_errors": [f"A subject with the updated subject_id and class_id already exists."]
                })
            raise

class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    permission_classes = [IsAdminOrSubAdmin]
    pagination_class = None
    lookup_field = 'unit_id'

    def get_queryset(self):
        queryset = Section.objects.all()
        class_id = self.request.query_params.get('class')
        subject_id = self.request.query_params.get('subject')
        if class_id and subject_id:
            try:
                class_id = int(class_id)
                subject_id = int(subject_id)
                queryset = queryset.filter(
                    subject__class_id=class_id,
                    subject__subject_id=subject_id
                )
            except ValueError:
                raise ValidationError({"non_field_errors": ["Query parameters 'class' and 'subject' must be valid integers."]})
        return queryset

    def perform_create(self, serializer):
        class_id = self.request.query_params.get('class')
        subject_id = self.request.query_params.get('subject')
        if not class_id or not subject_id:
            raise ValidationError(
                {"non_field_errors": ["Query parameters 'class' and 'subject' are required for creating a section."]})
        try:
            class_id = int(class_id)
            subject_id = int(subject_id)
        except ValueError:
            raise ValidationError(
                {"non_field_errors": ["Query parameters 'class' and 'subject' must be valid integers."]})
        subject = get_object_or_404(
            Subject,
            class_id=class_id,
            subject_id=subject_id
        )
        try:
            serializer.save(subject=subject)
        except IntegrityError as e:
            if "UNIQUE constraint failed: LearningApp_section.subject_id, LearningApp_section.unit_id" in str(e):
                raise ValidationError({
                    "non_field_errors": [
                        f"A section with unit_id={serializer.validated_data['unit_id']} already exists for subject_id={subject_id}."]
                })
            raise

    def perform_update(self, serializer):
        try:
            serializer.save()
        except IntegrityError as e:
            if "unique constraint" in str(e) and "subject_id_unit_id" in str(e):
                raise ValidationError({
                    "non_field_errors": [f"A section with the updated unit_id already exists for the subject."]
                })
            raise

class SyllabusViewSet(viewsets.ModelViewSet):
    serializer_class = SyllabusSerializer
    permission_classes = [IsAdminOrSubAdmin]
    pagination_class = None
    lookup_field = 'syllabus_id'

    def get_queryset(self):
        queryset = Syllabus.objects.all()
        class_id = self.request.query_params.get('class')
        subject_id = self.request.query_params.get('subject')
        unit_id = self.request.query_params.get('unit')
        if class_id and subject_id and unit_id:
            try:
                class_id = int(class_id)
                subject_id = int(subject_id)
                unit_id = int(unit_id)
                queryset = queryset.filter(
                    section__subject__class_id=class_id,
                    section__subject__subject_id=subject_id,
                    section__unit_id=unit_id
                )
            except ValueError:
                raise ValidationError({"non_field_errors": ["Query parameters 'class', 'subject', and 'unit' must be valid integers."]})
        return queryset

    def perform_create(self, serializer):
        class_id = self.request.query_params.get('class')
        subject_id = self.request.query_params.get('subject')
        unit_id = self.request.query_params.get('unit')
        if not class_id or not subject_id or not unit_id:
            raise ValidationError({"non_field_errors": ["Query parameters 'class', 'subject', and 'unit' are required for creating a syllabus."]})
        try:
            class_id = int(class_id)
            subject_id = int(subject_id)
            unit_id = int(unit_id)
        except ValueError:
            raise ValidationError({"non_field_errors": ["Query parameters 'class', 'subject', and 'unit' must be valid integers."]})
        section = get_object_or_404(
            Section,
            subject__class_id=class_id,
            subject__subject_id=subject_id,
            unit_id=unit_id
        )
        try:
            serializer.save(section=section)
        except IntegrityError:
            raise ValidationError({
                "non_field_errors": [
                    f"A syllabus with syllabus_id={serializer.validated_data.get('syllabus_id')} "
                    f"already exists for class_id={class_id}, subject_id={subject_id}, unit_id={unit_id}."
                ]
            })

    def perform_update(self, serializer):
        try:
            serializer.save()
        except IntegrityError as e:
            if "unique constraint" in str(e) and "section_id_syllabus_id" in str(e):
                raise ValidationError({
                    "non_field_errors": [f"A syllabus with the updated syllabus_id already exists for the section."]
                })
            raise



class SyllabusPartViewSet(viewsets.ModelViewSet):
    serializer_class = SyllabusPartSerializer
    permission_classes = [IsAdminOrSubAdmin]
    pagination_class = None
    lookup_field = 'part_id'

    def get_queryset(self):
        queryset = SyllabusPart.objects.all()
        syllabus_id = self.request.query_params.get('syllabus')
        class_id = self.request.query_params.get('class')
        subject_id = self.request.query_params.get('subject')
        unit_id = self.request.query_params.get('unit')
        if not (syllabus_id or (class_id and subject_id and unit_id)):
            raise ValidationError({
                "non_field_errors": ["Either 'syllabus' or 'class', 'subject', and 'unit' query parameters are required."]
            })
        if syllabus_id:
            try:
                syllabus_id = int(syllabus_id)
                if class_id and subject_id and unit_id:
                    try:
                        class_id = int(class_id)
                        subject_id = int(subject_id)
                        unit_id = int(unit_id)
                        section = get_object_or_404(
                            Section,
                            subject__class_id=class_id,
                            subject__subject_id=subject_id,
                            unit_id=unit_id
                        )
                        syllabus = get_object_or_404(
                            Syllabus,
                            syllabus_id=syllabus_id,
                            section=section
                        )
                    except ValueError:
                        raise ValidationError({"non_field_errors": ["Query parameters 'class', 'subject', and 'unit' must be valid integers."]})
                else:
                    syllabus = get_object_or_404(Syllabus, syllabus_id=syllabus_id)
                queryset = queryset.filter(syllabus=syllabus)
            except ValueError:
                raise ValidationError({"syllabus": "Query parameter 'syllabus' must be a valid integer."})
        elif class_id and subject_id and unit_id:
            try:
                class_id = int(class_id)
                subject_id = int(subject_id)
                unit_id = int(unit_id)
                syllabus = get_object_or_404(
                    Syllabus,
                    section__subject__class_id=class_id,
                    section__subject__subject_id=subject_id,
                    section__unit_id=unit_id
                )
                queryset = queryset.filter(syllabus=syllabus)
            except ValueError:
                raise ValidationError({"non_field_errors": ["Query parameters 'class', 'subject', and 'unit' must be valid integers."]})
        return queryset

    def perform_create(self, serializer):
        syllabus_id = self.request.query_params.get('syllabus')
        class_id = self.request.query_params.get('class')
        subject_id = self.request.query_params.get('subject')
        unit_id = self.request.query_params.get('unit')
        if not syllabus_id or not (class_id and subject_id and unit_id):
            raise ValidationError({
                "non_field_errors": ["Both 'syllabus' and 'class', 'subject', and 'unit' query parameters are required."]
            })
        try:
            syllabus_id = int(syllabus_id)
            class_id = int(class_id)
            subject_id = int(subject_id)
            unit_id = int(unit_id)
            section = get_object_or_404(
                Section,
                subject__class_id=class_id,
                subject__subject_id=subject_id,
                unit_id=unit_id
            )
            syllabus = get_object_or_404(
                Syllabus,
                syllabus_id=syllabus_id,
                section=section
            )
        except ValueError:
            raise ValidationError({
                "non_field_errors": ["Query parameters 'syllabus', 'class', 'subject', and 'unit' must be valid integers."]
            })
        try:
            serializer.save(syllabus=syllabus)
        except IntegrityError as e:
            raise ValidationError({"non_field_errors": [str(e)]})

    def perform_update(self, serializer):
        try:
            serializer.save()
        except IntegrityError as e:
            raise ValidationError({"non_field_errors": [str(e)]})