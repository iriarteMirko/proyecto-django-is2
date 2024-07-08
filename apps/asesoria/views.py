from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import AsesoriaSerializer
from .models import Asesoria, validar_asesoria
from .form import AsesoriaForm

class AsesoriaViewSet(viewsets.ModelViewSet):
    serializer_class = AsesoriaSerializer
    queryset = Asesoria.objects.all()

@login_required
def editar_asesoria(request, asesoria_id):
    asesoria = get_object_or_404(Asesoria, id=asesoria_id)
    curso = asesoria.curso
    if request.method == 'POST':
        error = validar_asesoria(request)
        if error:
            asesorias = curso.asesoria_set.all().order_by('fecha', 'hora_inicio')
            return render(request, 'curso/asesoria_curso.html', {'curso': curso, 'asesorias': asesorias, 'page': 'asesoria', 'error': error})
        form = AsesoriaForm(request.POST, instance=asesoria)
        if form.is_valid():
            form.save()
            return redirect('asesoria_curso', curso_id=curso.id, curso_slug=curso.slug)
    asesorias = curso.asesoria_set.all().order_by('fecha', 'hora_inicio')
    return render(request, 'curso/asesoria_curso.html', {'curso': curso, 'asesorias': asesorias, 'page': 'asesoria'})

@login_required
def eliminar_asesoria(request, asesoria_id):
    user = request.user
    if user.es_estudiante:
        return render(request, 'base/404.html')
    asesoria = get_object_or_404(Asesoria, id=asesoria_id)
    profesor = asesoria.curso.profesor
    if profesor != request.user.profesor:
        return render(request, 'base/404.html')
    asesoria.delete()
    return redirect('asesoria_curso', curso_id=asesoria.curso.id, curso_slug=asesoria.curso.slug)