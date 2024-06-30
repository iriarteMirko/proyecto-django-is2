from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'cursos', views.CursoViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('lista-de-cursos/', views.mis_cursos, name='cursos_profesor'),
    path('<int:curso_id>/<str:curso_nombre>/', views.detalle_curso, name='detalle_curso_profesor'),
    path('editar-curso/', views.editar_curso, name='editar_curso'),
    
]