from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model, logout
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

def mi_perfil(request):
    estudiante = request.user.estudiante
    return render(request, 'perfil_estudiante.html', {'estudiante': estudiante})

def editar_perfil(request):
    estudiante = request.user.estudiante
    return render(request, 'editar_perfil_estudiante.html', {'estudiante': estudiante})

def actualizar_perfil(request):
    user = request.user
    estudiante = user.estudiante
    User = get_user_model()
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        email = request.POST.get('email')
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        carrera = request.POST.get('carrera')
        ciclo = request.POST.get('ciclo')
        if codigo and email and nombre and apellidos and carrera and ciclo:
            if not codigo.isdigit():
                return render(request, 'editar_perfil_estudiante.html', {'estudiante': estudiante, 'error': 'El código debe ser un número entero.'})
            if codigo != user.codigo:
                if User.objects.filter(codigo=codigo).exists():
                    return render(request, 'editar_perfil_estudiante.html', {'estudiante': estudiante, 'error': 'El código ingresado ya está en uso.'})
            if email != user.email:
                if User.objects.filter(email=email).exists():
                    return render(request, 'editar_perfil_estudiante.html', {'estudiante': estudiante, 'error': 'El correo ingresado ya está en uso.'})
            user.codigo = codigo
            user.email = email
            user.nombre = nombre
            user.apellidos = apellidos
            estudiante.carrera = carrera
            estudiante.ciclo = ciclo
            estudiante.save()
            user.save()
            return redirect('perfil_estudiante')
        return render(request, 'editar_perfil_estudiante.html', {'estudiante': estudiante, 'error': 'Datos no válidos. Intente nuevamente.'})
    return render(request, 'editar_perfil_estudiante.html', {'estudiante': estudiante})

def cambiar_contrasena(request):
    user = request.user
    estudiante = user.estudiante
    if request.method == 'POST':
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if user.check_password(password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                logout(request)
                return redirect('signin')
            return render(request, 'editar_perfil_estudiante.html', {'estudiante': estudiante, 'error1': 'Las contraseñas no coinciden.'})
        return render(request, 'editar_perfil_estudiante.html', {'estudiante': estudiante, 'error1': 'Contraseña incorrecta.'})
    return render(request, 'editar_perfil_estudiante.html', {'estudiante': estudiante, 'error1': 'Datos no válidos. Intente nuevamente.'})

def eliminar_cuenta(request):
    user = request.user
    user.delete()
    return redirect('inicio')