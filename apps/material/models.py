from django.db import models
from apps.curso.models import Seccion

class Material(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='materiales/')
    seccion = models.ForeignKey(Seccion, related_name='materiales', on_delete=models.CASCADE)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
