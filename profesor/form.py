from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuario.models import Usuario
from .models import Profesor

class RegistroProfesorForm(UserCreationForm):
    profesion = forms.CharField(required=True)
    centro_laboral = forms.CharField(required=True)
    
    class Meta:
        model = Usuario
        fields = ('email', 'nombre', 'apellidos', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.usuario_profesor = True
        user.save()
        profesor = Profesor(
            usuario=user,
            profesion=self.cleaned_data['profesion'],
            centro_laboral=self.cleaned_data['centro_laboral'],
        )
        if commit:
            profesor.save()
        return user
