from django.urls import path
from . import views

urlpatterns = [
    path("post/", views.AboutUsClass.as_view(), name="about-us"),
    path("view/",views.AboutUsDetails.as_view(), name="about-us-name"),
]