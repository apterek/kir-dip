from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from api.tables.serializers import UserSerializer, PersonalSerializer, CameraSerializer, CabinetSerializer, \
    TimeStampSerializer
from core.models import Personal, Cameras, Cabinets, DateTimeStamp


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = []

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset


class PersonalViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalSerializer
    permission_classes = []
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Personal.objects.all()
        id_name = self.request.query_params.get("id")
        username = self.request.query_params.get('username')
        if id_name is not None and username is not None:
            queryset = queryset.filter(name=id_name, name__username=username)
            return queryset
        elif id_name is not None:
            queryset = queryset.filter(name=id_name)
            return queryset
        elif username is not None:
            queryset = queryset.filter(name__username=username)
            return queryset
        return queryset


class CamerasCabinetsView(viewsets.ModelViewSet):
    serializer_class = CameraSerializer
    permission_classes = []
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Cameras.objects.all()
        id_cam = self.request.query_params.get("id_cam")
        cab_id = self.request.query_params.get("cab_id")
        in_pos = self.request.query_params.get("in_pos")

        if id_cam is not None and cab_id is not None and in_pos is not None:
            queryset = queryset.filter(id_cam=id_cam, cab_id=cab_id, in_pos=in_pos)
            return queryset
        elif id_cam is not None and cab_id is not None:
            queryset = queryset.filter(id_cam=id_cam, cab_id=cab_id)
            return queryset
        elif id_cam is not None and in_pos is not None:
            queryset = queryset.filter(id_cam=id_cam, in_pos=in_pos)
            return queryset
        elif cab_id is not None and in_pos is not None:
            queryset = queryset.filter(cab_id=cab_id, in_pos=in_pos)
            return queryset
        elif id_cam is not None:
            queryset = queryset.filter(id_cam=id_cam)
            return queryset
        elif cab_id is not None:
            queryset = queryset.filter(cab_id=cab_id)
            return queryset
        elif in_pos is not None:
            queryset = queryset.filter(in_pos=in_pos)
            return queryset
        return queryset


class CabinetsView(viewsets.ModelViewSet):
    serializer_class = CabinetSerializer
    permission_classes = []
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Cabinets.objects.all()
        name = self.request.query_params.get("name")
        department = self.request.query_params.get("dep_id")
        if name is not None and department is not None:
            queryset = queryset.filter(name=name, dep_id=department)
            return queryset
        elif name is not None:
            queryset = queryset.filter(name=name)
            return queryset
        elif department is not None:
            queryset = queryset.filter(dep_id=department)
            return queryset
        return queryset


class TimeStampView(viewsets.ModelViewSet):
    queryset = DateTimeStamp.objects.order_by("timedate")[:10]
    serializer_class = TimeStampSerializer
    permission_classes = []
    http_method_names = ['get']
