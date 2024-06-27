from django.contrib import admin
from .models import Calificacion

class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['curso', 'estudiante', 'calificacion']
    
admin.site.register(Calificacion, CalificacionAdmin)
