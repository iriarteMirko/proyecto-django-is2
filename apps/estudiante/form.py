from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuario.models import Usuario
from .models import Estudiante

class RegistroEstudianteForm(UserCreationForm):
    carrera = forms.CharField(required=True)
    ciclo = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 13)], required=True)
    
    class Meta:
        model = Usuario
        fields = ('codigo', 'email', 'nombre', 'apellidos', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.es_estudiante = True
        user.save()
        estudiante = Estudiante(
            usuario=user,
            carrera=self.cleaned_data['carrera'],
            ciclo=self.cleaned_data['ciclo'],
        )
        if commit:
            estudiante.save()
        return user
