from django.urls import path
from .views import SchoolReviewListCreateView

urlpatterns = [
    path('school-reviews/', SchoolReviewListCreateView.as_view(), name='school-review-list-create'),
]
