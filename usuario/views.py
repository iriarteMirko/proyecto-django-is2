from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
        codigo = request.POST['codigo']
        password = request.POST['password']
        user = authenticate(request, username=codigo, password=password)
        if user is not None:
            login(request, user)
            if user.usuario_estudiante == True:
                return redirect('inicio_estudiante')
            return redirect('inicio_profesor')
        return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'Código o contraseña incorrectos.'})
    return render(request, 'signin.html', {'form': AuthenticationForm})

@login_required
def signout(request):
    logout(request)
    return redirect('signin')