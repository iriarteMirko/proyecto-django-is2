from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'profesor']

admin.site.register(Curso, CursoAdmin)
