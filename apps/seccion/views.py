from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import SeccionSerializer
from .models import Seccion
from .form import SeccionForm
from apps.usuario.decorators import VistaBase, ProfesorDecorator

class SeccionViewSet(viewsets.ModelViewSet):
    serializer_class = SeccionSerializer
    queryset = Seccion.objects.all()

class EditarSeccionVista(VistaBase):
    def procesar_solicitud(self, request, seccion_id, *args, **kwargs):
        seccion = get_object_or_404(Seccion, id=seccion_id)
        if request.method == 'POST':
            form = SeccionForm(request.POST, instance=seccion)
            if form.is_valid():
                form.save()
                return redirect('contenido_curso', curso_id=seccion.curso.id, curso_slug=seccion.curso.slug)
        curso = seccion.curso
        secciones = curso.secciones.all()
        return render(request, 'curso/contenido_curso.html', {'curso': curso, 'secciones': secciones, 'page': 'contenido'})

class EliminarSeccionVista(VistaBase):
    def procesar_solicitud(self, request, seccion_id, *args, **kwargs):
        seccion = get_object_or_404(Seccion, id=seccion_id)
        seccion.delete()
        return redirect('contenido_curso', curso_id=seccion.curso.id, curso_slug=seccion.curso.slug)

@login_required
def editar_seccion(request, seccion_id):
    vista = EditarSeccionVista()
    vistaDecorada = ProfesorDecorator(vista)
    return vistaDecorada.procesar_solicitud(request, seccion_id)

@login_required
def eliminar_seccion(request, seccion_id):
    vista = EliminarSeccionVista()
    vistaDecorada = ProfesorDecorator(vista)
    return vistaDecorada.procesar_solicitud(request, seccion_id)