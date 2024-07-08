from django.urls import path
from .views import agregar_material, eliminar_material

urlpatterns = [
    path('agregar/<int:seccion_id>/', agregar_material, name='agregar_material'),
    path('eliminar/<int:material_id>/', eliminar_material, name='eliminar_material'),
]
