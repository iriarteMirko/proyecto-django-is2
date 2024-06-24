from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'categoria', 'nivel', 'calificacion_promedio', 'fecha_creacion', 'ultima_modificacion', 'profesor']

admin.site.register(Curso, CursoAdmin)
