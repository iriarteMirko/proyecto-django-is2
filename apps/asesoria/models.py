from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.curso.models import Curso

class Asesoria(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField(blank=False, null=False, help_text="Fecha de la asesoría")
    hora_inicio = models.TimeField(blank=False, null=False, help_text="Hora de inicio de la asesoría")
    hora_fin = models.TimeField(blank=False, null=False, help_text="Hora de fin de la asesoría")
    enlace = models.URLField(max_length=250, blank=False, null=False, help_text="Enlace de la reunión")
    tema = models.CharField(max_length=200, blank=True, help_text="Tema principal de la asesoría")
    notas = models.TextField(max_length=500, blank=True, help_text="Notas adicionales sobre la asesoría")

    def __str__(self):
        return f"Asesoría de {self.curso.nombre}: {self.fecha} de {self.hora_inicio} a {self.hora_fin}"

    class Meta:
        verbose_name = "Asesoría"
        verbose_name_plural = "Asesorías"

    def clean(self):
        super().clean()
        fecha_hora_actual = timezone.now()
        fecha_hora_inicio = timezone.make_aware(timezone.datetime.combine(self.fecha, self.hora_inicio))
        fecha_hora_fin = timezone.make_aware(timezone.datetime.combine(self.fecha, self.hora_fin))

        if fecha_hora_inicio <= fecha_hora_actual:
            raise ValidationError("La fecha y hora de inicio deben ser mayores a la fecha y hora actual.")
        if fecha_hora_fin <= fecha_hora_inicio:
            raise ValidationError("La hora de fin debe ser mayor a la hora de inicio.")

@receiver(post_save, sender=Asesoria)
def auto_delete_past_asesoria(sender, instance, **kwargs):
    now = timezone.now()
    fecha_hora_fin = timezone.make_aware(timezone.datetime.combine(instance.fecha, instance.hora_fin))
    if fecha_hora_fin < now:
        instance.delete()
