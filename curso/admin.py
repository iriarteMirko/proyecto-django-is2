from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ['profesor', 'nombre', 'descripcion', 'categoria', 'nivel', 'calificacion', 'fecha_creacion', 'ultima_modificacion']

admin.site.register(Curso, CursoAdmin)
