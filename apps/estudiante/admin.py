from django.contrib import admin
from .models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'carrera', 'ciclo']

admin.site.register(Estudiante, EstudianteAdmin)