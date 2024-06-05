from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'categoria', 'profesor', 'fecha_creacion', 'ultima_modificacion']

admin.site.register(Curso, CursoAdmin)
