from django.shortcuts import render, redirect, get_object_or_404
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
        return render(request, 'curso/cursos_profesor.html', {'error2': 'Datos no válidos. Intente nuevamente.'})
    return render(request, 'curso/cursos_profesor.html')

@login_required
def crear_seccion(request, curso_id):
    factory = CursoConcreteFactory()
    if request.method == 'POST':
        from apps.curso.models import Curso
        curso = get_object_or_404(Curso, id=curso_id)
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        # Crear sección
        seccion = factory.create_seccion(curso=curso, nombre=nombre, descripcion=descripcion)
        if seccion:
            return redirect('contenido_curso', curso_id=curso.id, curso_nombre=curso.nombre)
        # Secciones del curso
        secciones = curso.seccion_set.all()
        return render(request, 'curso/contenido_curso.html', {'error': 'Datos no válidos. Intente nuevamente.', 'curso': curso, 'secciones': secciones})
    return render(request, 'curso/contenido_curso.html', {'curso': curso, 'secciones': secciones})

@login_required
def crear_asesoria(request, curso_id):
    factory = CursoConcreteFactory()
    if request.method == 'POST':
        from apps.curso.models import Curso
        from apps.asesoria.models import validar_asesoria
        curso = get_object_or_404(Curso, id=curso_id)
        error = validar_asesoria(request)
        if error:
            asesorias = curso.asesoria_set.all()
            return render(request, 'curso/asesoria_curso.html', {'curso': curso, 'asesorias': asesorias, 'error': error})
        fecha = request.POST.get('fecha')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fin = request.POST.get('hora_fin')
        enlace = request.POST.get('enlace')
        # Crear asesoría
        asesoria = factory.create_asesoria(curso=curso, fecha=fecha, hora_inicio=hora_inicio, hora_fin=hora_fin, enlace=enlace)
        if asesoria:
            return redirect('asesoria_curso', curso_id=curso.id, curso_nombre=curso.nombre)
        # Asesorías del curso
        asesorias = curso.asesoria_set.all()
        return render(request, 'curso/asesoria_curso.html', {'curso': curso, 'asesorias': asesorias, 'error': 'Datos no válidos. Intente nuevamente.'})
    return render(request, 'curso/asesoria_curso.html', {'curso': curso, 'asesorias': asesorias})
