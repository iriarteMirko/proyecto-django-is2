from django.db import models
from apps.seccion.models import Seccion

class Material(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    material = models.FileField(upload_to='materiales/')
    
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'
    
    def __str__(self):
        return f'{self.seccion.nombre} - {self.material}'