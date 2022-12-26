from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    id_dep = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


class Personal(models.Model):
    id_pers = models.AutoField(primary_key=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    dep_id = models.ForeignKey("Department", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"

    def __str__(self):
        return self.name.username


class Faces(models.Model):
    id_face = models.AutoField(primary_key=True)
    file = models.FileField(null=False)
    face_data = models.FileField(null=True, blank=True)
    pers_id = models.ForeignKey("Personal", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Faces"
        verbose_name_plural = "Faces"


class Cabinets(models.Model):
    id_cab = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100)
    floor = models.IntegerField()
    dep_id = models.ForeignKey("Department", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Cabinet"
        verbose_name_plural = "Cabinets"

    def __str__(self):
        return self.name


class Cameras(models.Model):
    id_cam = models.AutoField(primary_key=True)
    cam_model = models.CharField(null=False, max_length=100)
    addr = models.GenericIPAddressField()
    cab_id = models.ForeignKey("Cabinets", on_delete=models.CASCADE, blank=True, null=True)
    in_pos = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Cameras"
        verbose_name_plural = "Cameras"

    def __str__(self):
        return self.cam_model


class DateTimeStamp(models.Model):
    timedate = models.DateTimeField(null=False, auto_now_add=True, blank=True)
    per_id = models.ForeignKey("Personal", on_delete=models.CASCADE, blank=True, null=True)
    cab_id = models.ForeignKey("Cabinets", on_delete=models.CASCADE, blank=True, null=True)
    cam_id = models.ForeignKey("Cameras", on_delete=models.CASCADE, blank=True, null=True)
    direction = models.BooleanField(default=False)

    class Meta:
        verbose_name = "DateTimeStamp"
        verbose_name_plural = "DateTimeStamp"
