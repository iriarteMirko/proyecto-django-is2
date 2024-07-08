from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'inscripciones', views.InscripcionViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('curso/inscribir/<int:curso_id>/', views.inscribir_curso, name='inscribir_curso'),
    path('curso/retirar/<int:curso_id>/', views.retirar_curso, name='retirar_curso'),
    path('retirar-estudiante/<int:curso_id>/<int:estudiante_id>/', views.retirar_estudiante, name='retirar_estudiante'),
    
]