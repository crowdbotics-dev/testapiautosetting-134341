from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134341ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134341", Testconnectors134341ViewSet, basename="testconnectors134341"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
