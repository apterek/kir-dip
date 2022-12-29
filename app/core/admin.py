from django.contrib import admin
from core.models import Personal, Cabinets, Cameras, Faces, Department, DateTimeStamp

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ("id_pers","name", "dep_id")
    search_fields = ("id_pers","name__username", "dep_id__name")
    #readonly_fields = ("name", "dep_id")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


@admin.register(Cabinets)
class CabinetsAdmin(admin.ModelAdmin):
    list_display = ("id_cab","name", "floor", "dep_id", )
    search_fields = ("id_cab","name", "floor",  "dep_id__name")


@admin.register(Cameras)
class CamerasAdmin(admin.ModelAdmin):
    list_display = ("id_cam","cam_model", "addr", "cab_id", "in_pos", "status", )
    search_fields = ("id_cam","cam_model", "addr", "cab_id__name", "in_pos", "status", )


@admin.register(Faces)
class FacesAdmin(admin.ModelAdmin):
    list_display = ("file",  "pers_id", )
    search_fields = ("file", "pers_id__id_pers", )


@admin.register(DateTimeStamp)
class DateTimeStampAdmin(admin.ModelAdmin):
    list_display = ("timedate", "per_id", "cab_id", "cam_id", "direction", )
    search_fields = ("timedate", "per_id__id_pers", "cab_id__name", "cam_id__cam_model", "direction", )
