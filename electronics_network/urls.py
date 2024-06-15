from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import ElectronicsNetworkConfig
from .views import NetworkNodeViewSet

router = DefaultRouter()
router.register(r'nodes', NetworkNodeViewSet)

app_name = ElectronicsNetworkConfig.name

urlpatterns = [
    path('api/', include(router.urls)),
]
