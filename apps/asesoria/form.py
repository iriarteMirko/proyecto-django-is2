# apps/asesoria/forms.py

from django import forms
from .models import Asesoria

class AsesoriaForm(forms.ModelForm):
    class Meta:
        model = Asesoria
        fields = ('fecha', 'hora_inicio', 'hora_fin', 'enlace')
