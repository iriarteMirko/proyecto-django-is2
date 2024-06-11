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
    path('cursos/', views.mis_cursos, name='cursos_profesor'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('curso/<int:curso_id>/crear_seccion/', views.crear_seccion, name='crear_seccion'),
    
]
