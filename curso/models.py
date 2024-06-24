from django.db import models
from django.db.models import Avg
from profesor.models import Profesor
from estudiante.models import Estudiante

class Curso(models.Model):
    CATEGORIA_OPCIONES = [
        ('Desarrollo', 'Desarrollo'),
        ('Negocios', 'Negocios'),
        ('Finanzas', 'Finanzas'),
        ('Contabilidad', 'Contabilidad'),
        ('Informática y Software', 'Informática y Software'),
        ('Productividad', 'Productividad'),
        ('Diseño', 'Diseño'),
        ('Marketing', 'Marketing'),
        ('Economía', 'Economía'),
        ('Administración', 'Administración'),
        ('Derecho', 'Derecho'),
        ('Gestión de Proyectos', 'Gestión de Proyectos'),
    ]
    NIVEL_OPCIONES = [
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
        ('Experto', 'Experto'),
    ]
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(max_length=250, blank=True, null=True)
    categoria = models.CharField(max_length=100, choices=CATEGORIA_OPCIONES, blank=False, null=False)
    nivel = models.CharField(max_length=100, choices=NIVEL_OPCIONES, blank=False, null=False)
    calificacion_promedio = models.FloatField(default=0, editable=False)
    
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, through='inscripcion.Inscripcion')
    
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_modificacion = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
    def actualizar_calificacion_promedio(self):
        promedio = self.calificacion_set.aggregate(Avg('calificacion'))['calificacion__avg']
        self.calificacion_promedio = promedio if promedio is not None else 0
        self.save()