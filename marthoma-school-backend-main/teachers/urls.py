from django.urls import path
from .views import TeacherListCreateView, TeacherDetailView,TeacherProfileListCreateView,TeacherProfileDetailView

urlpatterns = [
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),

    # for testimonials
    path('teachers/profiles/', TeacherProfileListCreateView.as_view(), name='teacherprofile-list-create'),
    path('teachers/profiles/<int:pk>/', TeacherProfileDetailView.as_view(), name='teacherprofile-detail'),
]