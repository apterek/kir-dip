from django.contrib import admin
from core.models import Personal, Cabinets, Cameras, Faces, Department, DateTimeStamp

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ("name", "dep_id")
    search_fields = ("name", "dep_id")
    #readonly_fields = ("name", "dep_id")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


@admin.register(Cabinets)
class CabinetsAdmin(admin.ModelAdmin):
    list_display = ("name", "floor", "dep_id", )
    search_fields = ("name", "floor", "dep_id", )


@admin.register(Cameras)
class CamerasAdmin(admin.ModelAdmin):
    list_display = ("cam_model", "addr", "cab_id", "in_pos", "status", )
    search_fields = ("cam_model", "addr", "cab_id", "in_pos", "status", )


@admin.register(Faces)
class FacesAdmin(admin.ModelAdmin):
    list_display = ("file", "face_data", "pers_id", )
    search_fields = ("file", "face_data", "pers_id", )


@admin.register(DateTimeStamp)
class DateTimeStampAdmin(admin.ModelAdmin):
    list_display = ("timedate", "per_id", "cab_id", "cam_id", "direction", )
    search_fields = ("timedate", "per_id", "cab_id", "cam_id", "direction", )