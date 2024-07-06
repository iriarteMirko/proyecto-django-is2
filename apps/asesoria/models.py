from django.db import models
from apps.curso.models import Curso

class Asesoria(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="asesorias")
    fecha_hora = models.DateTimeField()
    duracion = models.DurationField(help_text="Duración en horas y minutos")
    enlace = models.URLField(max_length=200, help_text="Enlace de la reunión")
    tema = models.CharField(max_length=200, blank=True, help_text="Tema principal de la asesoría")
    notas = models.TextField(blank=True, help_text="Notas adicionales sobre la asesoría")

    def __str__(self):
        return f"Asesoría del curso {self.curso.nombre} el {self.fecha_hora.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Asesoría"
        verbose_name_plural = "Asesorías"
