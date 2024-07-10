from django.db import models
from apps.curso.models import Curso
from apps.estudiante.models import Estudiante


class Inscripcion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('curso', 'estudiante')
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'
    
    def __str__(self):
        return f'{self.estudiante.usuario.nombre} inscrito en {self.curso.nombre}'