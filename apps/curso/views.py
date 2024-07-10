from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializer import CursoSerializer
from .form import CursoForm
from .models import Curso
from apps.material.models import Material
from apps.usuario.decorators import VistaBase, ProfesorDecorator

class CursoViewSet(viewsets.ModelViewSet):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    lookup_field = 'slug'

class EditarCursoVista(VistaBase):
    def procesar_solicitud(self, request, curso_id, *args, **kwargs):
        curso = get_object_or_404(Curso, id=curso_id)
        if request.method == 'POST':
            form = CursoForm(request.POST, instance=curso)
            if form.is_valid():
                form.save()
        return redirect('informacion_curso', curso_id=curso.id, curso_slug=curso.slug)

class EliminarCursoVista(VistaBase):
    def procesar_solicitud(self, request, curso_id, *args, **kwargs):
        curso = get_object_or_404(Curso, id=curso_id)
        curso.delete()
        return redirect('lista_cursos')

@login_required
def mis_cursos(request):
    if request.user.es_profesor:
        cursos = Curso.objects.filter(profesor=request.user.profesor).order_by('fecha_creacion').reverse()
    else:
        from apps.inscripcion.models import Inscripcion
        inscripciones = Inscripcion.objects.filter(estudiante=request.user.estudiante)
        cursos = Curso.objects.filter(inscripcion__in=inscripciones).order_by('fecha_creacion').reverse()
    if not cursos:
        return render(request, 'curso/lista_cursos.html')
    paginator = Paginator(cursos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'curso/lista_cursos.html', {'page_obj': page_obj})

def buscar_cursos(request):
    query = request.GET.get('q', '')
    cursos = Curso.objects.filter(nombre__icontains=query).order_by('fecha_creacion').reverse()
    paginator = Paginator(cursos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'curso/buscar_cursos.html', {'page_obj': page_obj, 'query': query})

@login_required
def informacion_curso(request, curso_id, curso_slug):
    curso = get_object_or_404(Curso, id=curso_id, slug=curso_slug)
    is_inscrito = False
    if request.user.es_estudiante:
        from apps.inscripcion.models import Inscripcion
        is_inscrito = Inscripcion.objects.filter(curso=curso, estudiante=request.user.estudiante).exists()
    return render(request, 'curso/informacion_curso.html', {'curso': curso, 'page': 'informacion', 'is_inscrito': is_inscrito})

@login_required
def editar_curso(request, curso_id):
    vista = EditarCursoVista()
    vistaDecorator = ProfesorDecorator(vista)
    return vistaDecorator.procesar_solicitud(request, curso_id)

@login_required
def eliminar_curso(request, curso_id):
    vista = EliminarCursoVista()
    vistaDecorator = ProfesorDecorator(vista)
    return vistaDecorator.procesar_solicitud(request, curso_id)

@login_required
def contenido_curso(request, curso_id, curso_slug):
    curso = get_object_or_404(Curso, id=curso_id, slug=curso_slug)
    secciones = curso.seccion_set.all()
    materiales = Material.objects.filter(seccion__in=secciones)
    return render(request, 'curso/contenido_curso.html', {'curso': curso, 'secciones': secciones, 'materiales': materiales, 'page': 'contenido'})

@login_required
def asesoria_curso(request, curso_id, curso_slug):
    curso = get_object_or_404(Curso, id=curso_id, slug=curso_slug)
    asesorias = curso.asesoria_set.all().order_by('fecha', 'hora_inicio')
    return render(request, 'curso/asesoria_curso.html', {'curso': curso, 'asesorias': asesorias, 'page': 'asesoria'})

@login_required
def estudiantes_curso(request, curso_id, curso_slug):
    curso = get_object_or_404(Curso, id=curso_id, slug=curso_slug)
    inscripciones = curso.inscripcion_set.all()
    estudiantes = [inscripcion.estudiante for inscripcion in inscripciones]
    return render(request, 'curso/estudiantes_curso.html', {'curso': curso, 'estudiantes': estudiantes, 'page': 'estudiantes'})
