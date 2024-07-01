from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .factories import CursoConcreteFactory
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
            return render(request, 'profesor/signup_profesor.html', {'form': form, 'error': 'Datos no válidos. Intente nuevamente.'})
    else:
        form = RegistroProfesorForm()
    return render(request, 'profesor/signup_profesor.html', {'form': form})

@login_required
def inicio_profesor(request):
    return render(request, 'profesor/inicio_profesor.html')

@login_required
def crear_curso(request):
    factory = CursoConcreteFactory()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        categoria = request.POST.get('categoria')
        nivel = request.POST.get('nivel')
        profesor = request.user.profesor
        # Crear curso
        curso = factory.create_curso(nombre=nombre, descripcion=descripcion, categoria=categoria, nivel=nivel, profesor=profesor)
        if curso:
            return redirect('cursos_profesor')
        return render(request, 'profesor/cursos_profesor.html', {'error2': 'Datos no válidos. Intente nuevamente.'})
    return render(request, 'profesor/cursos_profesor.html')

@login_required
def crear_seccion(request, curso_id):
    factory = CursoConcreteFactory()
    if request.method == 'POST':
        from apps.curso.models import Curso
        curso = Curso.objects.get(id=curso_id)
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        # Crear sección
        seccion = factory.create_seccion(curso=curso, nombre=nombre, descripcion=descripcion)
        if seccion:
            return redirect('detalle_curso_profesor', curso_id=curso.id, curso_nombre=curso.nombre)
        return render(request, 'profesor/detalle_curso.html', {'error': 'Datos no válidos. Intente nuevamente.', 'curso': curso})
    return render(request, 'profesor/detalle_curso.html', {'curso': curso})
