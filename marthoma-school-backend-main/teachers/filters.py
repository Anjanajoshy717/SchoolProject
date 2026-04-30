import django_filters
from .models import Teacher

class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = ['category']