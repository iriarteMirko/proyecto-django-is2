from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('api/v1/', include(router.urls)),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('perfil/', views.mi_perfil, name='perfil'),
    path('perfil/<int:usuario_id>/<str:usuario_nombre>-<str:usuario_apellidos>/', views.ver_perfil, name='ver_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/actualizar/', views.actualizar_perfil, name='actualizar_perfil'),
    path('perfil/imagen/', views.cambiar_imagen, name='cambiar_imagen'),
    path('perfil/contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('perfil/eliminar/', views.eliminar_cuenta, name='eliminar_cuenta'),
    
]

# Configuración de la vista personalizada para errores 404
handler404 = 'apps.usuario.views.error_404_view'