from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'inscripciones', views.InscripcionViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('<int:curso_id>/<int:estudiante_id>/retirar-estudiante/', views.retirar_estudiante, name='retirar_estudiante'),
]