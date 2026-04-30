from django.urls import path
from .views import EnquiryCreateAPIView

urlpatterns = [
path('enquiry/', EnquiryCreateAPIView.as_view(), name='enquiry-form'),
]