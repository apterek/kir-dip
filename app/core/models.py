from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    age = models.IntegerField()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.first_name, self.last_name


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
    name = models.CharField(null=False, max_length=100)
    dep_id = models.ForeignKey("Department", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"

    def __str__(self):
        return self.name


class Faces(models.Model):
    id_face = models.AutoField(primary_key=True)
    file = models.FileField(null=False)
    face_data = models.FileField()
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


class Cameras(models.Model):
    id_cam = models.AutoField(primary_key=True)
    cam_model = models.CharField(null=False, max_length=100)
    addr = models.GenericIPAddressField()
    cab_id = models.ForeignKey("Cabinets", on_delete=models.CASCADE, blank=True, null=True)
    in_pos = models.BooleanField()

    class Meta:
        verbose_name = "Cameras"
        verbose_name_plural = "Cameras"


class DateTimeStamp(models.Model):
    timedate = models.DateTimeField(null=False, auto_now_add=True, blank=True)
    per_id = models.ForeignKey("Personal", on_delete=models.CASCADE, blank=True, null=True)
    cab_id = models.ForeignKey("Cabinets", on_delete=models.CASCADE, blank=True, null=True)
    cam_id = models.ForeignKey("Cameras", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "DateTimeStamp"
        verbose_name_plural = "DateTimeStamp"
