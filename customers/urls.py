from customers.views import CustomerViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r"customers", CustomerViewSet, basename="customer")

urlpatterns = router.urls
