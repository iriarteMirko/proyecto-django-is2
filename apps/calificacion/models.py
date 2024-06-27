from django.db import models
from apps.curso.models import Curso
from apps.estudiante.models import Estudiante
from apps.inscripcion.models import Inscripcion

class Calificacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])
    
    class Meta:
        unique_together = ('curso', 'estudiante')
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
    
    def __str__(self):
        return f'{self.curso.nombre} - {self.estudiante.usuario.nombre}: {self.calificacion}'

    def save(self, *args, **kwargs):
        if not Inscripcion.objects.filter(curso=self.curso, estudiante=self.estudiante).exists():
            raise ValueError("El estudiante debe estar inscrito en el curso para calificarlo.")
        super().save(*args, **kwargs)
        self.curso.actualizar_calificacion_promedio()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.curso.actualizar_calificacion_promedio()
