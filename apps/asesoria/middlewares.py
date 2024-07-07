from django.utils import timezone
from .models import Asesoria

class EliminarAsesoriasPasadasMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        now = timezone.now()
        asesorias = Asesoria.objects.all()
        for asesoria in asesorias:
            asesoria_datetime_fin = timezone.make_aware(timezone.datetime.combine(asesoria.fecha, asesoria.hora_fin))
            if asesoria_datetime_fin < now:
                asesoria.delete()
        
        response = self.get_response(request)
        return response