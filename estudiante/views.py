from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializer import EstudianteSerializer
from .models import Estudiante
from .form import RegistroEstudianteForm

class EstudianteViewSet(viewsets.ModelViewSet):
    serializer_class = EstudianteSerializer
    queryset = Estudiante.objects.all()

def signup_estudiante(request):
    if request.method == 'POST':
        form = RegistroEstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            codigo = form.cleaned_data.get('codigo')
            password = form.cleaned_data.get('password1')
            if not codigo.isdigit():
                return render(request, 'signup_estudiante.html', {'form': form, 'error': 'El código debe ser un número entero.'})
            user = authenticate(codigo=codigo, password=password)
            login(request, user)
            return redirect('inicio_estudiante')
        return render(request, 'signup_estudiante.html', {'form': form, 'error': 'Datos no válidos. Intente nuevamente.'})
    form = RegistroEstudianteForm()
    return render(request, 'signup_estudiante.html', {'form': form})

@login_required
def inicio_estudiante(request):
    return render(request, 'inicio_estudiante.html')

@login_required
def buscar_curso(request):
    from curso.models import Curso
    cursos = Curso.objects.all()
    paginator = Paginator(cursos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'buscar_cursos.html', {'page_obj': page_obj})

@login_required
def mis_cursos(request):
    return render(request, 'cursos_estudiante.html')

@login_required
def inscribir_curso(request, curso_id):
    from curso.models import Curso
    curso = get_list_or_404(Curso, id=curso_id)
    estudiante = request.user.estudiante
    curso.estudiantes.add(estudiante)
    return redirect('detalle_curso', curso_id=curso.id)

@login_required
def desinscribir_curso(request, curso_id):
    from curso.models import Curso
    curso = get_list_or_404(Curso, id=curso_id)
    estudiante = request.user.estudiante
    curso.estudiantes.remove(estudiante)
    return redirect('detalle_curso', curso_id=curso.id)

@login_required
def detalle_curso(request, curso_id):
    from curso.models import Curso
    curso = get_list_or_404(Curso, id=curso_id)
    return render(request, 'detalle_curso.html', {'curso': curso})

@login_required
def calificar_curso(request, curso_id):
    from curso.models import Curso
    from calificacion.models import Calificacion
    curso = get_list_or_404(Curso, id=curso_id)
    estudiante = request.user.estudiante
    if request.method == 'POST':
        calificacion_valor = int(request.POST.get('calificacion'))
        calificacion, created = Calificacion.objects.update_or_create(
            curso=curso,
            estudiante=estudiante,
            defaults={'calificacion': calificacion_valor},
        )
        curso.actualizar_calificacion_promedio()
        return redirect('detalle_curso', curso_id=curso.id)
    return render(request, 'calificacion/calificar_curso.html', {'curso': curso})
