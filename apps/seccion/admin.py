from django.contrib import admin
from .models import Seccion

# Register your models here.
class SeccionAdmin(admin.ModelAdmin):
    list_display = ['curso', 'nombre', 'descripcion']

admin.site.register(Seccion, SeccionAdmin)