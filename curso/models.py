from django.db import models
from profesor.models import Profesor

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre