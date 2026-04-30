from rest_framework import generics, permissions
from .models import Teacher, teachersprofview
from .serializers import TeacherSerializer, Teachersviewserializer
from .permissions import IsAdminOrReadOnly
from rest_framework import filters
from .filters import TeacherFilter # Import the filter class

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TeacherFilter
    search_fields = ['user__email', 'name', 'subject'] # Updated search field to use user's email
    ordering_fields = ['name', 'joining_date']

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminOrReadOnly]


class TeacherProfileListCreateView(generics.ListCreateAPIView):
    queryset = teachersprofview.objects.all()
    serializer_class = Teachersviewserializer
    permission_classes = [IsAdminOrReadOnly]

class TeacherProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = teachersprofview.objects.all()
    serializer_class = Teachersviewserializer
    permission_classes = [IsAdminOrReadOnly]