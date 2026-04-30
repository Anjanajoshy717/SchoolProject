from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EnquirySerializer
from rest_framework.permissions import AllowAny

from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

class EnquiryCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            enquiry = serializer.save()

            subject = f"New Enquiry from {enquiry.name}"
            message = f"""
            Name: {enquiry.name}
            Email: {enquiry.email}
            Phone Number: {enquiry.phone_number}
            Message: {enquiry.message}
            """
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['admin@example.com'],
                fail_silently=False,
            )

            return Response({'message': 'Enquiry submitted successfully.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)