from django.contrib import admin
from .models import Profesor

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'profesion', 'centro_laboral']

admin.site.register(Profesor, ProfesorAdmin)