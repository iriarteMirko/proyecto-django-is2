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
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        categoria = request.POST['categoria']
        profesor = request.user.profesor
        if nombre and descripcion and categoria:
            from curso.factories import CursoConcreteFactory
            factory = CursoConcreteFactory()
            curso = factory.create_curso(nombre, descripcion, categoria, profesor)
            if curso:
                return redirect('cursos_profesor')
            else:
                return render(request, 'cursos_profesor.html', {'error': 'Error al crear el curso. Intente nuevamente.'})
        else:
            return render(request, 'cursos_profesor.html', {'error': 'Datos no válidos. Intente nuevamente.'})
    return redirect('cursos_profesor')

def mi_perfil(request):
    profesor = request.user.profesor
    return render(request, 'perfil_profesor.html', {'profesor': profesor})