from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'estudiantes', views.EstudianteViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('signup/estudiante/', views.signup_estudiante, name='signup_estudiante'),
    path('inicio/', views.inicio_estudiante, name='inicio_estudiante'),
    path('perfil/', views.mi_perfil, name='perfil_estudiante'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil_estudiante'),
    path('perfil/actualizar/', views.actualizar_perfil, name='actualizar_perfil_estudiante'),
    path('cursos/buscar/', views.buscar_curso, name='buscar_cursos'),
    path('cursos/', views.mis_cursos, name='cursos_estudiante'),
    
]
