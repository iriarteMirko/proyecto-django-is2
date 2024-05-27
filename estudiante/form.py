from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuario.models import Usuario
from .models import Estudiante

class RegistroEstudianteForm(UserCreationForm):
    universidad = forms.CharField(required=True)
    carrera = forms.CharField(required=True)
    ciclo = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 13)], required=True)
    codigo = forms.CharField(required=True)
    
    class Meta:
        model = Usuario
        fields = ('email', 'nombre', 'apellidos', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.usuario_estudiante = True
        user.save()
        estudiante = Estudiante(
            usuario=user,
            universidad=self.cleaned_data['universidad'],
            carrera=self.cleaned_data['carrera'],
            ciclo=self.cleaned_data['ciclo'],
            codigo=self.cleaned_data['codigo'],
        )
        if commit:
            estudiante.save()
        return user
