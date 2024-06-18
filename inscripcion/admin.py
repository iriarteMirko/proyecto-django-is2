from django.contrib import admin
from .models import Inscripcion

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['curso', 'estudiante', 'fecha_inscripcion']

admin.site.register(Inscripcion, InscripcionAdmin)