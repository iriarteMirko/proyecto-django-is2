from django.db import models
from usuario.models import Usuario

class Profesor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    profesion = models.CharField(max_length=100, blank=False, null=False)
    centro_laboral = models.CharField(max_length=100, blank=False, null=False)
    
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
    
    def __str__(self):
        return f'{self.usuario.nombre} {self.usuario.apellidos}'
