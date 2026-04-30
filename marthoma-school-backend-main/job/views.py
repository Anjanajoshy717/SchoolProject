from rest_framework import viewsets, permissions,filters
from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer
import datetime
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-posted_at')
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_active']
    search_fields = ['title', 'job_type', 'department', 'subject'] 

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
    def get_queryset(self):
        # First, update all jobs in the database
        today = datetime.date.today()
        
        # Set is_active=False for all jobs whose last_date has passed
        Job.objects.filter(last_date__lt=today, is_active=True).update(is_active=False)
        
        # # Set is_active=True for all jobs whose last_date is today or in the future
        # Job.objects.filter(last_date__gte=today, is_active=False).update(is_active=True)

        queryset = Job.objects.all().order_by('-posted_at')
        
        # If the user is not an admin, filter to only show active jobs
        if not self.request.user.is_staff:
            return queryset.filter(is_active=True)
        # If the user is an admin, show all jobs
        return queryset
       
class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['job']

    def get_permissions(self):
        # Anyone can create (submit) an application
        if self.action == 'create':
            return [permissions.AllowAny()]
        # Only admins can view, update, or delete applications
        return [permissions.IsAdminUser()]
# class JobViewSet(viewsets.ModelViewSet):
#     # queryset = Job.objects.filter(is_active=True).order_by('-posted_at')
#     queryset = Job.objects.all().order_by('-posted_at') 
#     serializer_class = JobSerializer
#     filter_backends = [DjangoFilterBackend,filters.SearchFilter]
#     filterset_fields = ['is_active']
#     search_fields = ['title', 'job_type', 'department', 'subject']  

#     def get_permissions(self):
#         if self.action in ['create', 'update', 'partial_update', 'destroy']:
#             return [permissions.IsAdminUser()] 
#         return [permissions.AllowAny()]  


# # class JobApplicationViewSet(viewsets.ModelViewSet):
# #     queryset = JobApplication.objects.all()
# #     serializer_class = JobApplicationSerializer
# #     permission_classes = [permissions.AllowAny]
# class JobApplicationViewSet(viewsets.ModelViewSet):
#     queryset = JobApplication.objects.all()
#     serializer_class = JobApplicationSerializer
#     # This line is crucial: it restricts access to admin users only
#     permission_classes = [permissions.IsAdminUser] 