from django.db import models
from apps.curso.models import Curso

class Seccion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='secciones')
    nombre = models.CharField(max_length=30, blank=False, null=False)
    descripcion = models.TextField(max_length=500)
    
    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'
    
    def __str__(self):
        return self.curso.nombre + ' - ' + self.nombre