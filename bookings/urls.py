from bookings.views import BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"bookings", BookingViewSet, basename="booking")

urlpatterns = router.urls
