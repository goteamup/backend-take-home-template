from rest_framework.routers import DefaultRouter

from classes.views import ClassSessionViewSet, ClassTypeViewSet

router = DefaultRouter()
router.register(r"class_sessions", ClassSessionViewSet, basename="class_session")
router.register(r"class_types", ClassTypeViewSet, basename="class_type")

urlpatterns = router.urls
