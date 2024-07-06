from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.curso.models import Curso

class Asesoria(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="asesorias")
    fecha = models.DateField(help_text="Fecha de la asesoría")
    hora_inicio = models.TimeField(help_text="Hora de inicio de la asesoría")
    hora_fin = models.TimeField(help_text="Hora de fin de la asesoría")
    enlace = models.URLField(max_length=250, help_text="Enlace de la reunión")
    tema = models.CharField(max_length=200, blank=True, help_text="Tema principal de la asesoría")
    notas = models.TextField(max_length=500, blank=True, help_text="Notas adicionales sobre la asesoría")

    def __str__(self):
        return f"Asesoría del curso {self.curso.nombre} el {self.fecha} de {self.hora_inicio} a {self.hora_fin}"

    class Meta:
        verbose_name = "Asesoría"
        verbose_name_plural = "Asesorías"

@receiver(post_save, sender=Asesoria)
def auto_delete_past_asesoria(sender, instance, **kwargs):
    """Automatically deletes past asesorias after they are saved or updated."""
    now = timezone.now()
    current_datetime = timezone.make_aware(timezone.datetime.combine(instance.fecha, instance.hora_fin))
    if current_datetime < now:
        instance.delete()
