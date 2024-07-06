from django.contrib import admin
from .models import Asesoria

class AsesoriaAdmin(admin.ModelAdmin):
    list_display = ['curso', 'fecha_hora', 'duracion', 'enlace', 'tema', 'notas']
    
admin.site.register(Asesoria, AsesoriaAdmin)