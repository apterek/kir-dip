from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from api.tables.serializers import UserSerializer, PersonalSerializer, CameraSerializer, CabinetSerializer, TimeStampSerializer
from core.models import Personal, Cameras, Cabinets, DateTimeStamp


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']


class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    permission_classes = []
    http_method_names = ['get']


class CamerasCabinetsView(viewsets.ModelViewSet):
    queryset = Cameras.objects.all()
    serializer_class = CameraSerializer
    permission_classes = []
    http_method_names = ['get']


class CabinetsView(viewsets.ModelViewSet):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer
    permission_classes = []
    http_method_names = ['get']


class TimeStampView(viewsets.ModelViewSet):
    queryset = DateTimeStamp.objects.order_by("timedate")[:10]
    serializer_class = TimeStampSerializer
    permission_classes = []
    http_method_names = ['get']
