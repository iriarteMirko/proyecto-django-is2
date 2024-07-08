from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'inscripciones', views.InscripcionViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('curso/<int:curso_id>/inscribir/', views.inscribir_curso, name='inscribir_curso'),
    path('curso/<int:curso_id>/desinscribir/', views.retirar_curso, name='desinscribir_curso'),
    path('<int:curso_id>/<int:estudiante_id>/retirar-estudiante/', views.retirar_estudiante, name='retirar_estudiante'),
    
]