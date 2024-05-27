from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.utils import timezone
from rest_framework import viewsets
from .serializer import UsuarioSerializer
from .models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

def inicio(request):
    return render(request, 'inicio.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        password = request.POST['password']
        user = authenticate(request, username=correo, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'Correo o contraseña incorrectos.'})
    return render(request, 'signin.html', {'form': AuthenticationForm})

@login_required
def signout(request):
    logout(request)
    return redirect('inicio')