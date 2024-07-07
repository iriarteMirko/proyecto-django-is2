from django.db import models
from apps.usuario.models import Usuario
from django.core.exceptions import ValidationError

class Profesor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    profesion = models.CharField(max_length=25, blank=False, null=False)
    centro_laboral = models.CharField(max_length=25, blank=False, null=False)
    
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
    
    def __str__(self):
        return f'{self.usuario.nombre} {self.usuario.apellidos}'
    
    def clean(self):
        if self.usuario.es_estudiante:
            raise ValidationError("El usuario no puede ser profesor y estudiante al mismo tiempo.")
