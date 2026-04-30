from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from .permissions import IsAdminOrSubadminOrReadOnly  # Custom permission class

# GET (everyone), POST (admin/subadmin)
class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all().order_by('-published_at')  # Latest news first
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrSubadminOrReadOnly]

# GET (everyone), PUT/PATCH/DELETE (admin/subadmin)
class NewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrSubadminOrReadOnly]
