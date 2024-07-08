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
