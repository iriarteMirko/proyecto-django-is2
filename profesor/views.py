from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from rest_framework import viewsets
from .serializer import ProfesorSerializer
from .models import Profesor
from .form import RegistroProfesorForm

class ProfesorViewSet(viewsets.ModelViewSet):
    serializer_class = ProfesorSerializer
    queryset = Profesor.objects.all()

def signup_profesor(request):
    if request.method == 'POST':
        form = RegistroProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            codigo = form.cleaned_data.get('codigo')
            password = form.cleaned_data.get('password1')
            user = authenticate(codigo=codigo, password=password)
            login(request, user)
            return redirect('inicio_profesor')
        else:
            return render(request, 'signup_profesor.html', {'form': form, 'error': 'Datos no válidos. Intente nuevamente.'})
    else:
        form = RegistroProfesorForm()
    return render(request, 'signup_profesor.html', {'form': form})

def inicio_profesor(request):
    return render(request, 'inicio_profesor.html')

def mis_cursos(request):
    from curso.models import Curso
    cursos = Curso.objects.all()
    cursos_prof = [curso for curso in cursos if curso.profesor == request.user.profesor]
    
    return render(request, 'cursos_profesor.html', {'cursos': cursos_prof})

def crear_curso(request):
    from curso.factories import CursoConcreteFactory
    factory = CursoConcreteFactory()
    if request.method == 'POST':
        curso = factory.create_curso(request.POST['nombre'], request.POST['descripcion'], request.POST['categoria'], request.user.profesor)
        if curso:
            return redirect('cursos_profesor')
        return render(request, 'crear_curso.html', {'error': 'Datos no válidos. Intente nuevamente.'})
    return render(request, 'crear_curso.html')

def mi_perfil(request):
    profesor = request.user.profesor
    return render(request, 'perfil_profesor.html', {'profesor': profesor})