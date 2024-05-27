from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
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
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('inicio_estudiante')
        else:
            return render(request, 'signup_estudiante.html', {'form': form, 'error': 'Datos no válidos. Intente nuevamente.'})
    else:
        form = RegistroEstudianteForm()
    return render(request, 'signup_estudiante.html', {'form': form})

def inicio_estudiante(request):
    return render(request, 'inicio_estudiante.html')

def mis_cursos(request):
    return render(request, 'cursos_estudiante.html')