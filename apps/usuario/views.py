from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rest_framework import viewsets
from .serializer import UsuarioSerializer
from .models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    lookup_field = 'slug'

def inicio(request):
    return render(request, 'usuario/inicio.html')

@login_required
def inicio_user(request):
    user = request.user
    cursos_inscritos = []
    asesorias_disponibles = []
    cursos_creados = []
    estudiantes_inscritos = []
    if user.es_estudiante:
        from apps.inscripcion.models import Inscripcion
        from apps.asesoria.models import Asesoria
        inscripciones = Inscripcion.objects.filter(estudiante=user.estudiante)
        cursos_inscritos = [inscripcion.curso for inscripcion in inscripciones]
        asesorias_disponibles = Asesoria.objects.filter(curso__in=cursos_inscritos)
    elif user.es_profesor:
        from apps.curso.models import Curso
        from apps.estudiante.models import Estudiante
        cursos_creados = Curso.objects.filter(profesor=user.profesor)
        estudiantes_inscritos = Estudiante.objects.filter(inscripcion__curso__in=cursos_creados).distinct()
    context = {
        'user': user,
        'cursos_inscritos': cursos_inscritos,
        'asesorias_disponibles': asesorias_disponibles,
        'cursos_creados': cursos_creados,
        'estudiantes_inscritos': estudiantes_inscritos,
    }
    return render(request, 'usuario/inicio_user.html', context)

def signup(request):
    return render(request, 'usuario/signup.html')

def signin(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        password = request.POST['password']
        user = authenticate(request, username=codigo, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff == True:
                return redirect(reverse('admin:index'))
            return redirect('inicio_user')
        return render(request, 'usuario/signin.html', {'form': AuthenticationForm, 'error': 'Código o contraseña incorrectos.'})
    return render(request, 'usuario/signin.html', {'form': AuthenticationForm})

@login_required
def signout(request):
    logout(request)
    return redirect('signin')

@login_required
def mi_perfil(request):
    user = request.user
    contexto = {'user': user}
    if user.es_estudiante:
        estudiante = user.estudiante
        contexto['estudiante'] = estudiante
    elif user.es_profesor:
        profesor = user.profesor
        contexto['profesor'] = profesor
    return render(request, 'usuario/perfil.html', contexto)

def ver_perfil(request, usuario_id, usuario_slug):
    user = get_object_or_404(Usuario, id=usuario_id)
    contexto = {'user': user}
    if user.es_estudiante:
        estudiante = user.estudiante
        inscripciones = estudiante.inscripcion_set.all()
        contexto['estudiante'] = estudiante
        contexto['inscripciones'] = inscripciones
    elif user.es_profesor:
        profesor = user.profesor
        cursos = profesor.curso_set.all()
        contexto['profesor'] = profesor
        contexto['cursos'] = cursos
    return render(request, 'usuario/ver_perfil.html', contexto)

@login_required
def editar_perfil(request):
    user = request.user
    contexto = {'user': user}
    if user.es_estudiante:
        estudiante = user.estudiante
        contexto['estudiante'] = estudiante
    elif user.es_profesor:
        profesor = user.profesor
        contexto['profesor'] = profesor
    return render(request, 'usuario/editar_perfil.html', contexto)

def validar_datos(request, user):
    codigo = request.POST.get('codigo')
    email = request.POST.get('email')
    nombre = request.POST.get('nombre')
    apellidos = request.POST.get('apellidos')
    if not (codigo and email and nombre and apellidos):
        return None, 'Datos no válidos. Intente nuevamente.'
    if len(codigo) != 8:
        return None, 'El código debe tener 8 dígitos.'
    if not codigo.isdigit():
        return None, 'El código debe ser un número entero.'
    User = get_user_model()
    if codigo != user.codigo and User.objects.filter(codigo=codigo).exists():
        return None, 'El código ingresado ya está en uso.'
    if email != user.email and User.objects.filter(email=email).exists():
        return None, 'El correo ingresado ya está en uso.'
    return {
        'codigo': codigo,
        'email': email,
        'nombre': nombre,
        'apellidos': apellidos
    }, None

@login_required
def actualizar_perfil(request):
    user = request.user
    if request.method == 'POST':
        datos_comunes, error = validar_datos(request, user)
        if error:
            if user.es_estudiante:
                estudiante = user.estudiante
                return render(request, 'usuario/editar_perfil.html', {'estudiante': estudiante, 'error': error})
            profesor = user.profesor
            return render(request, 'usuario/editar_perfil.html', {'profesor': profesor, 'error': error})
        user.codigo = datos_comunes['codigo']
        user.email = datos_comunes['email']
        user.nombre = datos_comunes['nombre']
        user.apellidos = datos_comunes['apellidos']
        
        if user.es_estudiante:
            estudiante = user.estudiante
            carrera = request.POST.get('carrera')
            ciclo = request.POST.get('ciclo')
            if carrera and ciclo:
                estudiante.carrera = carrera
                estudiante.ciclo = ciclo
                estudiante.save()
            else:
                return render(request, 'usuario/editar_perfil.html', {'estudiante': estudiante, 'error': 'Datos no válidos. Intente nuevamente.'})
            user.save()
            return redirect('perfil')
        elif user.es_profesor:
            profesor = user.profesor
            profesion = request.POST.get('profesion')
            centro_laboral = request.POST.get('centro_laboral')
            if profesion and centro_laboral:
                profesor.profesion = profesion
                profesor.centro_laboral = centro_laboral
                profesor.save()
            else:
                return render(request, 'usuario/editar_perfil.html', {'profesor': profesor, 'error': 'Datos no válidos. Intente nuevamente.'})
            user.save()
            return redirect('perfil')
        
    contexto = {'user': user}
    if user.es_estudiante:
        estudiante = user.estudiante
        contexto['estudiante'] = estudiante
    elif user.es_profesor:
        profesor = user.profesor
        contexto['profesor'] = profesor
    
    return render(request, 'usuario/editar_perfil.html', contexto)

@login_required
def cambiar_imagen(request):
    user = request.user
    if request.method == 'POST':
        imagen = request.FILES.get('imagen')
        user.imagen = imagen
        user.save()
        return redirect('perfil')
    return render(request, 'usuario/editar_perfil.html', {'user': user, 'error1': 'Datos no válidos. Intente nuevamente.'})

def validar_password(password):
    if len(password) < 8:
        return 'La contraseña debe tener al menos 8 caracteres.'
    if password.isdigit() or password.isalpha():
        return 'La contraseña debe tener al menos un número y una letra.'
    if password.islower() or password.isupper():
        return 'La contraseña debe tener al menos una letra mayúscula y una minúscula.'
    return None

@login_required
def cambiar_contrasena(request):
    user = request.user
    contexto = {'user': user}
    if user.es_estudiante:
        estudiante = user.estudiante
        contexto['estudiante'] = estudiante
    elif user.es_profesor:
        profesor = user.profesor
        contexto['profesor'] = profesor
    if request.method == 'POST':
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if user.check_password(password):
            if new_password == confirm_password:
                error = validar_password(new_password)
                if error:
                    contexto['error2'] = error
                    return render(request, 'usuario/editar_perfil.html', contexto)
                user.set_password(new_password)
                user.save()
                logout(request)
                return redirect('signin')
            contexto['error2'] = 'Las contraseñas no coinciden.'
            return render(request, 'usuario/editar_perfil.html', contexto)
        contexto['error2'] = 'Contraseña incorrecta.'
        return render(request, 'usuario/editar_perfil.html', contexto)
    contexto['error2'] = 'Datos no válidos. Intente nuevamente.'
    return render(request, 'usuario/editar_perfil.html', contexto)

@login_required
def eliminar_cuenta(request):
    user = request.user
    user.delete()
    return redirect('inicio')

def error_404_view(request, exception):
    user = request.user
    return render(request, 'base/404.html', {'user': user, 'exception': exception}, status=404)