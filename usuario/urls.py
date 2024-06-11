from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('perfil/actualizar/', views.actualizar_perfil, name='actualizar_perfil'),
    path('perfil/contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('perfil/eliminar/', views.eliminar_cuenta, name='eliminar_cuenta'),
    path('api/v1/', include(router.urls)),
]
