from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'secciones', views.SeccionViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('<int:seccion_id>/editar-seccion/', views.editar_seccion, name='editar_seccion'),
    path('<int:seccion_id>/eliminar-seccion/', views.eliminar_seccion, name='eliminar_seccion'),
]