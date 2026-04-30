from rest_framework import generics, permissions
from .models import SchoolReview
from .serializers import SchoolReviewSerializer

class SchoolReviewListCreateView(generics.ListCreateAPIView):
    queryset = SchoolReview.objects.all().order_by('-created_at')
    serializer_class = SchoolReviewSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
