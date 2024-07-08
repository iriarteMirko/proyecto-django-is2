from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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
            return redirect('inicio_user')
        return render(request, 'estudiante/signup_estudiante.html', {'form': form, 'error': 'Datos no válidos. Intente nuevamente.'})
    form = RegistroEstudianteForm()
    return render(request, 'estudiante/signup_estudiante.html', {'form': form})

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
