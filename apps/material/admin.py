from django.contrib import admin
from .models import Material

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['seccion', 'material']

admin.site.register(Material, MaterialAdmin)