from django.urls import path, include
from rest_framework import routers
from . import views

# Versionado de la API
router = routers.DefaultRouter()
router.register(r'materiales', views.MaterialViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('<int:seccion_id>/agregar-material/', views.agregar_material, name='agregar_material'),
    path('<int:material_id>/eliminar-material/', views.eliminar_material, name='eliminar_material'),
    
]