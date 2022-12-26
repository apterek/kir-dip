from django.urls import include, path
from rest_framework import routers, views
from api.tables.views import UserViewSet, PersonalViewSet, CamerasCabinetsView, CabinetsView, TimeStampView
"""from api.products.views import ProductsViewSet
from api.users.views import RegisterViewSet, LoginView, LogoutView
from api.purchase.views import PurchaseViewSet, PurchaseUserViewSet, AddPurchaseViewSet"""


app_name = "api"

router = routers.DefaultRouter()
router.register(r"personal", PersonalViewSet, "personal")
router.register(r"users", UserViewSet, "users")
router.register(r"cameras", CamerasCabinetsView, "cameras")
router.register(r"cabinets", CabinetsView, "cabinets")

router.register(r"time", TimeStampView, "time")
"""router.register(r"login", LoginView, "login")
router.register(r"logout", LogoutView, "logout")

router.register(r"purchase", PurchaseViewSet, "purchases")
router.register(r"user", PurchaseUserViewSet, "user")
router.register(r"add_purchase", AddPurchaseViewSet, "add_purchase")"""


urlpatterns = [
    path("", include(router.urls)),
]
