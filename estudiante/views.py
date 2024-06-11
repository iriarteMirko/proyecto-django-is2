from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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

def inicio_estudiante(request):
    return render(request, 'inicio_estudiante.html')

def buscar_curso(request):
    from curso.models import Curso
    cursos = Curso.objects.all()
    paginator = Paginator(cursos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'buscar_cursos.html', {'page_obj': page_obj})

def mis_cursos(request):
    return render(request, 'cursos_estudiante.html')