from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'estudiantes', views.EstudianteViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('signup/estudiante/', views.signup_estudiante, name='signup_estudiante'),
    
]