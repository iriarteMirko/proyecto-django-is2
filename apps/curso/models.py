from django.db import models
from django.utils.text import slugify
from apps.profesor.models import Profesor

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
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    categoria = models.CharField(max_length=100, choices=CATEGORIA_OPCIONES, blank=False, null=False)
    nivel = models.CharField(max_length=100, choices=NIVEL_OPCIONES, blank=False, null=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_modificacion = models.DateField(auto_now=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=False, blank=True)
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super(Curso, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre