from rest_framework import viewsets
from rest_framework.response import Response
from .models import SportEvent, SportImage, Winner
from .serializers import SportEventSerializer, SportImageSerializer, WinnerSerializer
from .permissions import IsAdminOrSubAdmin


class SportEventViewSet(viewsets.ModelViewSet):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventSerializer
    permission_classes = [IsAdminOrSubAdmin]


class SportImageViewSet(viewsets.ModelViewSet):
    queryset = SportImage.objects.all()
    serializer_class = SportImageSerializer
    permission_classes = [IsAdminOrSubAdmin]


class WinnerViewSet(viewsets.ModelViewSet):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer
    permission_classes = [IsAdminOrSubAdmin]
