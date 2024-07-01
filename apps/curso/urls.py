from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'cursos', views.CursoViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('lista-de-cursos/', views.mis_cursos, name='cursos_profesor'),
    path('<int:curso_id>/<str:curso_nombre>/detalle-curso/', views.detalle_curso, name='detalle_curso_profesor'),
    path('<int:curso_id>/<str:curso_nombre>/informacion-curso/', views.informacion_curso, name='informacion_curso'),
    path('<int:curso_id>/editar-curso/', views.editar_curso, name='editar_curso'),
    path('<int:curso_id>/eliminar-curso/', views.eliminar_curso, name='eliminar_curso'),
    path('<int:curso_id>/<str:curso_nombre>/contenido-curso/', views.contenido_curso, name='contenido_curso'),
    path('<int:curso_id>/<str:curso_nombre>/asesoria-curso/', views.asesoria_curso, name='asesoria_curso'),
    
]