from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'estudiantes', views.EstudianteViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('signup/estudiante/', views.signup_estudiante, name='signup_estudiante'),
    path('cursos/buscar/', views.buscar_curso, name='buscar_cursos'),
    path('cursos/', views.mis_cursos, name='cursos_estudiante'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso_estudiante'),
    path('curso/<int:curso_id>/inscribir/', views.inscribir_curso, name='inscribir_curso'),
    path('curso/<int:curso_id>/desinscribir/', views.desinscribir_curso, name='desinscribir_curso'),
    
]