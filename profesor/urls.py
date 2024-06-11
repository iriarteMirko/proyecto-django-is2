from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'profesores', views.ProfesorViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('signup/profesor/', views.signup_profesor, name='signup_profesor'),
    path('inicio/', views.inicio_profesor, name='inicio_profesor'),
    path('perfil/', views.mi_perfil, name='perfil_profesor'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil_profesor'),
    path('cursos/', views.mis_cursos, name='cursos_profesor'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    
]
