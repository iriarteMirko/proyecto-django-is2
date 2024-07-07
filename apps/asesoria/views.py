from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import AsesoriaSerializer
from .models import Asesoria
from .form import AsesoriaForm

class AsesoriaViewSet(viewsets.ModelViewSet):
    serializer_class = AsesoriaSerializer
    queryset = Asesoria.objects.all()

@login_required
def editar_asesoria(request, asesoria_id):
    asesoria = get_object_or_404(Asesoria, id=asesoria_id)
    if request.method == 'POST':
        form = AsesoriaForm(request.POST, instance=asesoria)
        if form.is_valid():
            form.save()
            return redirect('asesoria_curso', curso_id=asesoria.curso.id, curso_nombre=asesoria.curso.nombre)
    curso = asesoria.curso
    asesorias = curso.asesoria_set.all().order_by('fecha', 'hora_inicio')
    return render(request, 'curso/asesoria_curso.html', {'curso': curso, 'asesorias': asesorias, 'page': 'asesoria'})

@login_required
def eliminar_asesoria(request, asesoria_id):
    asesoria = get_object_or_404(Asesoria, id=asesoria_id)
    asesoria.delete()
    return redirect('asesoria_curso', curso_id=asesoria.curso.id, curso_nombre=asesoria.curso.nombre)