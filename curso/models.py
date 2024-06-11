from django.db import models
from estudiante.admin import Estudiante
from profesor.models import Profesor

class Curso(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(max_length=250, blank=False, null=False)
    categoria = models.CharField(max_length=100, blank=False, null=False)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_modificacion = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.nombre