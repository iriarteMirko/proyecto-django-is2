from django.contrib import admin
from .models import Calificacion

class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['curso', 'usuario', 'calificacion', 'fecha_creacion', 'ultima_modificacion']
    
admin.site.register(Calificacion, CalificacionAdmin)
