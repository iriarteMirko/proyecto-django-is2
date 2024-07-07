from django.contrib import admin
from .models import Material

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'archivo', 'seccion', 'fecha_subida']

admin.site.register(Material, MaterialAdmin)
