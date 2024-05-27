from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'profesores', views.ProfesorViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('signup/profesor/', views.signup_profesor, name='signup_profesor'),
]
