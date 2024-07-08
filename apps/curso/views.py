from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializer import CursoSerializer
from .form import CursoForm
from .models import Curso

class CursoViewSet(viewsets.ModelViewSet):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    lookup_field = 'slug'

@login_required
def mis_cursos(request):
    if request.user.es_profesor:
        cursos = Curso.objects.filter(profesor=request.user.profesor).order_by('fecha_creacion').reverse()
    else:
        cursos = Curso.objects.filter(estudiantes=request.user.estudiante).order_by('fecha_creacion').reverse()
    if not cursos:
        return render(request, 'curso/lista_cursos.html')
    paginator = Paginator(cursos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'curso/lista_cursos.html', {'page_obj': page_obj})

@login_required
def informacion_curso(request, curso_id, curso_slug):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'curso/informacion_curso.html', {'curso': curso, 'page': 'informacion'})

@login_required
def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
    return redirect('informacion_curso', curso_id=curso.id, curso_slug=curso.slug)

@login_required
def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.delete()
    return redirect('lista_cursos')

@login_required
def contenido_curso(request, curso_id, curso_slug):
    curso = get_object_or_404(Curso, id=curso_id)
    secciones = curso.seccion_set.all()
    return render(request, 'curso/contenido_curso.html', {'curso': curso, 'secciones': secciones, 'page': 'contenido'})

@login_required
def asesoria_curso(request, curso_id, curso_slug):
    curso = get_object_or_404(Curso, id=curso_id)
    asesorias = curso.asesoria_set.all().order_by('fecha', 'hora_inicio')
    return render(request, 'curso/asesoria_curso.html', {'curso': curso, 'asesorias': asesorias, 'page': 'asesoria'})

@login_required
def estudiantes_curso(request, curso_id, curso_slug):
    curso = get_object_or_404(Curso, id=curso_id)
    inscripciones = curso.inscripcion_set.all()
    estudiantes = [inscripcion.estudiante for inscripcion in inscripciones]
    return render(request, 'curso/estudiantes_curso.html', {'curso': curso, 'estudiantes': estudiantes, 'page': 'estudiantes'})
