from django.contrib import admin
from .models import Asesoria

class AsesoriaAdmin(admin.ModelAdmin):
    list_display = ['curso', 'fecha', 'hora_inicio', 'hora_fin', 'enlace' , 'tema', 'notas']
    
admin.site.register(Asesoria, AsesoriaAdmin)