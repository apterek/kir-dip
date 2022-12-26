from django.urls import include, path
from rest_framework import routers
from api.tables.views import UserViewSet, PersonalViewSet, CamerasCabinetsView, CabinetsView, TimeStampView
from api.users.views import RegisterViewSet, LoginView, LogoutView

app_name = "api"

router = routers.DefaultRouter()
router.register(r"personal", PersonalViewSet, "personal")
router.register(r"users", UserViewSet, "users")
router.register(r"cameras", CamerasCabinetsView, "cameras")
router.register(r"cabinets", CabinetsView, "cabinets")
router.register(r"time", TimeStampView, "time")

router.register(r"register", RegisterViewSet, "register")
router.register(r"login", LoginView, "login")
router.register(r"logout", LogoutView, "logout")

urlpatterns = [
    path("", include(router.urls)),
]
