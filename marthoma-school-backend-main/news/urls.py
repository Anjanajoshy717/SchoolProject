from django.urls import path
from .views import NewsListCreateView, NewsRetrieveUpdateDestroyView

urlpatterns = [
    # This maps to: /api/news/ → List all or Create new news
    path('', NewsListCreateView.as_view(), name='news-list-create'),

    # This maps to: /api/news/<id>/ → Retrieve, Update or Delete a specific news
    path('<int:pk>/', NewsRetrieveUpdateDestroyView.as_view(), name='news-detail'),
]
