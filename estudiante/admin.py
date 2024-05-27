from django.contrib import admin
from .models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'universidad', 'carrera', 'ciclo', 'codigo']

admin.site.register(Estudiante, EstudianteAdmin)