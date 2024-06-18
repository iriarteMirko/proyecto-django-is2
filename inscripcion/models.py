from django.db import models
from curso.models import Curso
from estudiante.models import Estudiante


class Inscripcion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.estudiante.usuario.username} inscrito en {self.curso.nombre}'