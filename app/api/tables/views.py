from django.contrib.auth.models import User
from rest_framework import viewsets

from api.tables.serializers import UserSerializer, PersonalSerializer, CameraSerializer, CabinetSerializer, TimeStampSerializer
from core.models import Personal, Cameras, Cabinets, DateTimeStamp


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    permission_classes = []


class CamerasCabinetsView(viewsets.ModelViewSet):
    queryset = Cameras.objects.all()
    serializer_class = CameraSerializer
    permission_classes = []


class CabinetsView(viewsets.ModelViewSet):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer
    permission_classes = []


class TimeStampView(viewsets.ModelViewSet):
    queryset = DateTimeStamp.objects.order_by("timedate")[:10]
    serializer_class = TimeStampSerializer
    permission_classes = []
