from django.http import HttpResponseForbidden

class VistaBase:
    def procesar_solicitud(self, request, *args, **kwargs):
        pass

class ProfesorDecorator(VistaBase):
    def __init__(self, vista_envuelta):
        self.vista_envuelta = vista_envuelta
        
    def procesar_solicitud(self, request, *args, **kwargs):
        if not request.user.es_profesor:
            return HttpResponseForbidden("Acceso denegado.")
        return self.vista_envuelta.procesar_solicitud(request, *args, **kwargs)

class EstudianteDecorator(VistaBase):
    def __init__(self, vista_envuelta):
        self.vista_envuelta = vista_envuelta
        
    def procesar_solicitud(self, request, *args, **kwargs):
        if not request.user.es_estudiante:
            return HttpResponseForbidden("Acceso denegado.")
        return self.vista_envuelta.procesar_solicitud(request, *args, **kwargs)