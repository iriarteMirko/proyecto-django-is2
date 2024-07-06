from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'asesoria', views.AsesoriaViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]