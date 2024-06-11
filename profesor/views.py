from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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
            return render(request, 'signup_profesor.html', {'form': form, 'error': 'Datos no válidos. Intente nuevamente.'})
    else:
        form = RegistroProfesorForm()
    return render(request, 'signup_profesor.html', {'form': form})

@login_required
def inicio_profesor(request):
    return render(request, 'inicio_profesor.html')

@login_required
def mis_cursos(request):
    from curso.models import Curso
    cursos = Curso.objects.filter(profesor=request.user.profesor)
    paginator = Paginator(cursos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'cursos_profesor.html', {'page_obj': page_obj})

@login_required
def crear_curso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        categoria = request.POST.get('categoria')
        profesor = request.user.profesor
        if nombre and descripcion and categoria:
            factory = CursoConcreteFactory()
            curso = factory.create_curso(nombre, descripcion, categoria, profesor)
            if curso:
                return redirect('cursos_profesor')
            else:
                return render(request, 'cursos_profesor.html', {'error': 'Error al crear el curso. Intente nuevamente.'})
        else:
            return render(request, 'cursos_profesor.html', {'error': 'Datos no válidos. Intente nuevamente.'})
    return redirect('cursos_profesor')