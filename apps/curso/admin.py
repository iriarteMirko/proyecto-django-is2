from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'categoria', 'nivel', 'fecha_creacion', 'ultima_modificacion', 'profesor', 'slug']

admin.site.register(Curso, CursoAdmin)
