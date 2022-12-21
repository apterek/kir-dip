from django.urls import include, path
from rest_framework import routers
"""from api.posts.views import PostViewSet
from api.products.views import ProductsViewSet
from api.users.views import RegisterViewSet, LoginView, LogoutView
from api.purchase.views import PurchaseViewSet, PurchaseUserViewSet, AddPurchaseViewSet"""


app_name = "api"

router = routers.DefaultRouter()
"""router.register(r"posts", PostViewSet, "posts")
router.register(r"products", ProductsViewSet, "products")

router.register(r"register", RegisterViewSet, "register")
router.register(r"login", LoginView, "login")
router.register(r"logout", LogoutView, "logout")

router.register(r"purchase", PurchaseViewSet, "purchases")
router.register(r"user", PurchaseUserViewSet, "user")
router.register(r"add_purchase", AddPurchaseViewSet, "add_purchase")"""


urlpatterns = [
    path("", include(router.urls)),
]