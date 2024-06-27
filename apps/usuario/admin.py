from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'email', 'nombre', 'apellidos', 'activo', 'es_estudiante', 'es_profesor', 'es_administrador']

admin.site.register(Usuario, UsuarioAdmin)