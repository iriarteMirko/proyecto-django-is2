from django.db import models
from usuario.models import Usuario

class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    carrera = models.CharField(max_length=100, blank=False, null=False)
    ciclo = models.PositiveIntegerField(blank=False, null=False, choices=[(i, i) for i in range(1, 13)])
    
    def __str__(self):
        return f'{self.usuario.nombre} {self.usuario.apellidos}'
