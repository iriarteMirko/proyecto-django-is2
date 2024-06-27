from django.shortcuts import render, redirect, get_object_or_404
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
                return render(request, 'estudiante/signup_estudiante.html', {'form': form, 'error': 'El código debe ser un número entero.'})
            user = authenticate(codigo=codigo, password=password)
            login(request, user)
            return redirect('inicio_estudiante')
        return render(request, 'estudiante/signup_estudiante.html', {'form': form, 'error': 'Datos no válidos. Intente nuevamente.'})
    form = RegistroEstudianteForm()
    return render(request, 'estudiante/signup_estudiante.html', {'form': form})

@login_required
def inicio_estudiante(request):
    return render(request, 'estudiante/inicio_estudiante.html')

@login_required
def buscar_curso(request):
    from apps.curso.models import Curso
    cursos = Curso.objects.all()
    paginator = Paginator(cursos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'estudiante/buscar_cursos.html', {'page_obj': page_obj})

@login_required
def mis_cursos(request):
    from apps.inscripcion.models import Inscripcion
    inscripciones = Inscripcion.objects.filter(estudiante=request.user.estudiante).order_by('fecha_inscripcion')
    if not inscripciones:
        return render(request, 'estudiante/cursos_estudiante.html')
    cursos = [inscripcion.curso for inscripcion in inscripciones]
    return render(request, 'estudiante/cursos_estudiante.html', {'cursos': cursos})

@login_required
def detalle_curso(request, curso_id):
    from apps.curso.models import Curso
    curso = get_object_or_404(Curso, id=curso_id)
    secciones = curso.seccion_set.all()
    return render(request, 'estudiante/detalle_curso.html', {'curso': curso, 'secciones': secciones})


@login_required
def inscribir_curso(request, curso_id):
    from apps.curso.models import Curso
    curso = get_object_or_404(Curso, id=curso_id)
    estudiante = request.user.estudiante
    curso.estudiantes.add(estudiante)
    return redirect('detalle_curso', curso_id=curso.id)

@login_required
def desinscribir_curso(request, curso_id):
    from apps.curso.models import Curso
    curso = get_object_or_404(Curso, id=curso_id)
    estudiante = request.user.estudiante
    curso.estudiantes.remove(estudiante)
    return redirect('detalle_curso', curso_id=curso.id)

@login_required
def calificar_curso(request, curso_id):
    from apps.curso.models import Curso
    from apps.calificacion.models import Calificacion
    curso = get_object_or_404(Curso, id=curso_id)
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
    return render(request, 'estudiante/calificar_curso.html', {'curso': curso})
