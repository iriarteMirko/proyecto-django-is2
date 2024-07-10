from django.db import models
from apps.seccion.models import Seccion

class Material(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name='materiales')
    nombre = models.CharField(max_length=30, blank=True, null=True)
    archivo = models.FileField(upload_to='materiales/', blank=False, null=False)
    
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'
    
    def __str__(self):
        return f'Material: {self.nombre} de la sección {self.seccion.nombre}'