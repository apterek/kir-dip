from rest_framework import serializers
from core.models import Personal, Department, Cameras, Cabinets, DateTimeStamp
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "last_name", "first_name"]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["name"]


class PersonalSerializer(serializers.ModelSerializer):
    name = UserSerializer()
    dep_id = DepartmentSerializer()

    class Meta:
        model = Personal
        fields = ["id_pers", "name", "dep_id"]


class CamerasCabinetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinets
        fields = ["name"]


class CameraSerializer(serializers.ModelSerializer):
    cab_id = CamerasCabinetsSerializer()

    class Meta:
        model = Cameras
        fields = ["id_cam", "cam_model", "cab_id", "in_pos"]


class CabinetSerializer(serializers.ModelSerializer):
    dep_id = DepartmentSerializer()

    class Meta:
        model = Cabinets
        fields = ["id_cab", "name", "floor", "dep_id"]


class TimeStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTimeStamp
        fields = "__all__"
