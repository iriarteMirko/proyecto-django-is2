from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'asesorias', views.AsesoriaViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('<int:asesoria_id>/editar-asesoria/', views.editar_asesoria, name='editar_asesoria'),
    path('<int:asesoria_id>/eliminar-asesoria/', views.eliminar_asesoria, name='eliminar_asesoria'),
]