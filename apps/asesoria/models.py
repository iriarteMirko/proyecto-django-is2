from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from apps.curso.models import Curso

class Asesoria(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField(blank=False, null=False, help_text="Fecha de la asesoría")
    hora_inicio = models.TimeField(blank=False, null=False, help_text="Hora de inicio de la asesoría")
    hora_fin = models.TimeField(blank=False, null=False, help_text="Hora de fin de la asesoría")
    enlace = models.URLField(max_length=200, blank=False, null=False, help_text="Enlace de la reunión")
    
    class Meta:
        verbose_name = "Asesoría"
        verbose_name_plural = "Asesorías"
    
    def __str__(self):
        return f"Asesoría de {self.curso.nombre} - {self.fecha} de {self.hora_inicio} a {self.hora_fin}"
    
    def clean(self):
        super().clean()
        datetime_actual = timezone.now()
        datetime_inicio = timezone.make_aware(timezone.datetime.combine(self.fecha, self.hora_inicio))
        datetime_fin = timezone.make_aware(timezone.datetime.combine(self.fecha, self.hora_fin))
        
        if datetime_inicio <= datetime_actual:
            raise ValidationError("La fecha y hora de inicio deben ser mayores a la fecha y hora actual.")
        if datetime_fin <= datetime_inicio:
            raise ValidationError("La hora de fin debe ser mayor a la hora de inicio.")