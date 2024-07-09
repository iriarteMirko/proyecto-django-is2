from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import InscripcionSerializer
from .models import Inscripcion
from apps.curso.models import Curso
from apps.usuario.decorators import VistaBase, EstudianteDecorator, ProfesorDecorator

class InscripcionViewSet(viewsets.ModelViewSet):
    serializer_class = InscripcionSerializer
    queryset = Inscripcion.objects.all()

class InscripcionVista(VistaBase):
    def procesar_solicitud(self, request, curso_id, *args, **kwargs):
        curso = get_object_or_404(Curso, id=curso_id)
        estudiante = request.user.estudiante
        inscripcion = Inscripcion.objects.create(curso=curso, estudiante=estudiante)
        if inscripcion:
            return redirect('informacion_curso', curso_id=curso.id, curso_slug=curso.slug)
        return redirect('buscar_cursos')

class RetirarInscripcionVista(VistaBase):
    def procesar_solicitud(self, request, curso_id, *args, **kwargs):
        curso = get_object_or_404(Curso, id=curso_id)
        estudiante = request.user.estudiante
        inscripcion = get_object_or_404(Inscripcion, curso=curso, estudiante=estudiante)
        inscripcion.delete()
        return redirect('buscar_cursos')

class RetirarEstudianteVista(VistaBase):
    def procesar_solicitud(self, request, curso_id, estudiante_id, *args, **kwargs):
        curso = get_object_or_404(Curso, id=curso_id)
        inscripcion = get_object_or_404(Inscripcion, curso=curso, estudiante_id=estudiante_id)
        inscripcion.delete()
        return redirect('estudiantes_curso', curso_id=curso.id, curso_slug=curso.slug)

@login_required
def inscribir_curso(request, curso_id):
    vista = InscripcionVista()
    vistaDecorator = EstudianteDecorator(vista)
    return vistaDecorator.procesar_solicitud(request, curso_id)

@login_required
def retirar_curso(request, curso_id):
    vista = RetirarInscripcionVista()
    vistaDecorator = EstudianteDecorator(vista)
    return vistaDecorator.procesar_solicitud(request, curso_id)

@login_required
def retirar_estudiante(request, curso_id, estudiante_id):
    vista = RetirarEstudianteVista()
    vistaDecorator = ProfesorDecorator(vista)
    return vistaDecorator.procesar_solicitud(request, curso_id, estudiante_id)
