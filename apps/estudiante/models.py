from django.db import models
from apps.usuario.models import Usuario
from django.core.exceptions import ValidationError

class Estudiante(models.Model):
    CARRERA_OPCIONES = [
        ('Arquitectura', 'Arquitectura'),
        ('Administración', 'Administración'),
        ('Contabilidad y Finanzas', 'Contabilidad y Finanzas'),
        ('Economía', 'Economía'),
        ('Marketing', 'Marketing'),
        ('Negocios Internacionales', 'Negocios Internacionales'),
        ('Comunicación', 'Comunicación'),
        ('Derecho', 'Derecho'),
        ('Ingeniería Civil', 'Ingeniería Civil'),
        ('Ingeniería Industrial', 'Ingeniería Industrial'),
        ('Ingeniería de Sistemas', 'Ingeniería de Sistemas'),
        ('Psicología', 'Psicología'),
    ]
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    carrera = models.CharField(max_length=100, choices=CARRERA_OPCIONES, blank=False, null=False)
    ciclo = models.PositiveIntegerField(blank=False, null=False, choices=[(i, i) for i in range(1, 13)])
    
    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
    
    def __str__(self):
        return f'{self.usuario.nombre} {self.usuario.apellidos}'
    
    def clean(self):
        if self.usuario.es_profesor:
            raise ValidationError("El usuario no puede ser estudiante y profesor al mismo tiempo.")
