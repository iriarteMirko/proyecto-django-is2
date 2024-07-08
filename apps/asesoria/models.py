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

def validar_profesor(request, asesoria):
    user = request.user
    if user.es_estudiante:
        return "No tienes permisos para realizar esta acción."
    profesor = asesoria.curso.profesor
    if profesor != request.user.profesor:
        return "No tienes permisos para realizar esta acción."
    return None

def validar_asesoria(request):
    from datetime import datetime
    fecha_str = request.POST.get('fecha')
    hora_inicio_str = request.POST.get('hora_inicio')
    hora_fin_str = request.POST.get('hora_fin')
    enlace = request.POST.get('enlace')
    
    fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
    hora_inicio = datetime.strptime(hora_inicio_str, '%H:%M').time()
    hora_fin = datetime.strptime(hora_fin_str, '%H:%M').time()
    
    datetime_actual = timezone.now()
    datetime_inicio = timezone.make_aware(datetime.combine(fecha, hora_inicio))
    datetime_fin = timezone.make_aware(datetime.combine(fecha, hora_fin))
    
    if datetime_inicio <= datetime_actual:
        return "La fecha y hora de inicio deben ser mayores a la fecha y hora actual."
    if datetime_fin <= datetime_inicio:
        return "La hora de fin debe ser mayor a la hora de inicio."
    if not enlace:
        return "El enlace de la reunión es requerido."
    return None