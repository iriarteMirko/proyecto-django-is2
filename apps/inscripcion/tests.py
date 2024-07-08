# apps/inscripcion/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.profesor.models import Profesor
from apps.curso.models import Curso
from apps.estudiante.models import Estudiante
from .models import Inscripcion

class InscripcionModelTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(codigo='20191627', email='20191627@aloe.ulima.edu.pe', nombre='Juan', apellidos='Gutiérrez', password='Elpapi12')
        self.profesor_user = User.objects.create_user(codigo='20191629', email='profesor@ulima.edu.pe', nombre='Luis', apellidos='Pérez', password='profesor123')
        self.profesor = Profesor.objects.create(usuario=self.profesor_user, profesion='Ingeniero', centro_laboral='Universidad de Lima')
        self.curso = Curso.objects.create(
            nombre='Matemáticas',
            descripcion='Curso de matemáticas avanzadas',
            categoria='Desarrollo',
            nivel='Intermedio',
            profesor=self.profesor
        )
        self.estudiante = Estudiante.objects.create(
            usuario=self.user,
            carrera='Comunicación',
            ciclo=9
        )

    def test_crear_inscripcion(self):
        inscripcion = Inscripcion.objects.create(
            curso=self.curso,
            estudiante=self.estudiante
        )
        self.assertEqual(inscripcion.curso.nombre, 'Matemáticas')
        self.assertEqual(inscripcion.estudiante.usuario.nombre, 'Juan')
