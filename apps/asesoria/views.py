from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import AsesoriaSerializer
from .models import Asesoria, validar_profesor, validar_asesoria
from .form import AsesoriaForm
from apps.usuario.decorators import VistaBase, ProfesorDecorator

class AsesoriaViewSet(viewsets.ModelViewSet):
    serializer_class = AsesoriaSerializer
    queryset = Asesoria.objects.all()

class EditarAsesoriaVista(VistaBase):
    def procesar_solicitud(self, request, asesoria_id, *args, **kwargs):
        asesoria = get_object_or_404(Asesoria, id=asesoria_id)
        if request.method == 'POST':
            error = validar_profesor(request, asesoria)
            if error:
                return render(request, 'base/404.html', {'error': error})
            error = validar_asesoria(request)
            if error:
                asesorias = asesoria.curso.asesorias.all().order_by('fecha', 'hora_inicio')
                return render(request, 'curso/asesoria_curso.html', {'curso': asesoria.curso, 'asesorias': asesorias, 'page': 'asesoria', 'error': error})
            form = AsesoriaForm(request.POST, instance=asesoria)
            if form.is_valid():
                form.save()
        return redirect('asesoria_curso', curso_id=asesoria.curso.id, curso_slug=asesoria.curso.slug)

class EliminarAsesoriaVista(VistaBase):
    def procesar_solicitud(self, request, asesoria_id, *args, **kwargs):
        asesoria = get_object_or_404(Asesoria, id=asesoria_id)
        error = validar_profesor(request, asesoria)
        if error:
            return render(request, 'base/404.html', {'error': error})
        asesoria.delete()
        return redirect('asesoria_curso', curso_id=asesoria.curso.id, curso_slug=asesoria.curso.slug)

@login_required
def editar_asesoria(request, asesoria_id):
    vista = EditarAsesoriaVista()
    vistaDecorada = ProfesorDecorator(vista)
    return vistaDecorada.procesar_solicitud(request, asesoria_id)

@login_required
def eliminar_asesoria(request, asesoria_id):
    vista = EliminarAsesoriaVista()
    vistaDecorada = ProfesorDecorator(vista)
    return vistaDecorada.procesar_solicitud(request, asesoria_id)