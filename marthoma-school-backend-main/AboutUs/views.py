from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import AboutUsSerialization
from .models import AboutUsModel
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class AboutUsClass(GenericAPIView):
    # School Information posting
    def post(self, request):
        serializer = AboutUsSerialization(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":"success",
                "message":"Information added",
                "data":serializer.data
            }, status=status.HTTP_200_OK)

class AboutUsDetails(GenericAPIView):
    def get(self, request):
        obj = AboutUsModel.objects.first()  # or use get() if you expect exactly one
        if obj:
            serializer = AboutUsSerialization(obj)
            return Response({
                "status": "success",
                "message": "Fetched About Us",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "failed",
                "message": "No About Us data found"
            }, status=status.HTTP_404_NOT_FOUND)

    # School Information Updation full/ partially
    def put(self, request):
        serializer = AboutUsModel.objects.first()
        if not serializer:
            return Response({
                "status": "error",
                "message": "Failed to update About Us info"
            }, status=status.HTTP_400_BAD_REQUEST)

        obj = AboutUsSerialization(
            instance=serializer,
            data=request.data,
            partial=True
        )

        if obj.is_valid():
            obj.save()
            return Response({
                "status": "success",
                "message": "About Us info updated successfully!",
                "data": obj.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "failed",
                "message": "Failed to update About Us info",
                "error": obj.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    # School Info Deletion fully
    def delete(self, request):
        obj = AboutUsModel.objects.first()
        if obj is not None:
            obj.delete()
            return Response({
                "status": "success",
                "message": "About Us all info deleted!",
            }, status=status.HTTP_200_OK)

        return Response({
            "status": "failed",
            "message": "failed to delete About Us info",
        }, status=status.HTTP_400_BAD_REQUEST)


