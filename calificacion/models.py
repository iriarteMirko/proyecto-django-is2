from django.db import models
from curso.models import Curso
from estudiante.models import Estudiante

class Calificacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])
    
    class Meta:
        unique_together = ('curso', 'estudiante')
    
    def __str__(self):
        return f'{self.curso.nombre} - {self.estudiante.usuario.nombre}: {self.calificacion}'