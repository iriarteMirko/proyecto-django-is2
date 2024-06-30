from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializer import CursoSerializer
from .models import Curso

class CursoViewSet(viewsets.ModelViewSet):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()

@login_required
def mis_cursos(request):
    cursos = Curso.objects.filter(profesor=request.user.profesor).order_by('ultima_modificacion')
    if not cursos:
        return render(request, 'curso/cursos_profesor.html')
    paginator = Paginator(cursos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'curso/cursos_profesor.html', {'page_obj': page_obj})

@login_required
def detalle_curso(request, curso_id, curso_nombre):
    curso = get_object_or_404(Curso, id=curso_id)
    secciones = curso.seccion_set.all()
    print(curso_nombre)
    return render(request, 'curso/detalle_curso.html', {'curso': curso, 'secciones': secciones})

@login_required
def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('detalle_curso', curso_id=curso.id, curso_nombre=curso.nombre)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso/editar_curso.html', {'form': form})