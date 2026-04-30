from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsAdminOrReadOnly
from django.shortcuts import get_object_or_404

class AdvertisementListCreateAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        ads = Advertisement.objects.all()
        if not ads.exists():
            return Response(
                {"detail": "No data found", },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = AdvertisementSerializer(ads, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvertisementDetailAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Advertisement, pk=pk)

    def get(self, request, pk):
        ad = self.get_object(pk)
        serializer = AdvertisementSerializer(ad)
        return Response(serializer.data)

    def put(self, request, pk):
        ad = self.get_object(pk)
        serializer = AdvertisementSerializer(ad, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ad = self.get_object(pk)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
