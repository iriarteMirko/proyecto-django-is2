from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import InscripcionSerializer
from .models import Inscripcion
from apps.curso.models import Curso

class InscripcionViewSet(viewsets.ModelViewSet):
    serializer_class = InscripcionSerializer
    queryset = Inscripcion.objects.all()

@login_required
def inscribir_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    estudiante = request.user.estudiante
    curso.estudiantes.add(estudiante)
    return redirect('detalle_curso', curso_id=curso.id)

@login_required
def retirar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    estudiante = request.user.estudiante
    curso.estudiantes.remove(estudiante)
    return redirect('detalle_curso', curso_id=curso.id)

@login_required
def retirar_estudiante(request, curso_id, estudiante_id):
    curso = get_object_or_404(Curso, id=curso_id)
    inscripcion = get_object_or_404(Inscripcion, curso=curso, estudiante_id=estudiante_id)
    inscripcion.delete()
    return redirect('estudiantes_curso', curso_id=curso.id, curso_slug=curso.slug)
