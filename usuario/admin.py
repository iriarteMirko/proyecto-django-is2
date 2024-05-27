from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['email', 'nombre', 'apellidos', 'usuario_activo', 'usuario_estudiante', 'usuario_profesor', 'usuario_administrador']

admin.site.register(Usuario, UsuarioAdmin)