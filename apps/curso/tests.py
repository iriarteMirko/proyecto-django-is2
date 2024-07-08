# apps/curso/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.profesor.models import Profesor
from .models import Curso

class CursoModelTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.profesor_user = User.objects.create_user(codigo='20191629', email='profesor@ulima.edu.pe', nombre='Luis', apellidos='Pérez', password='profesor123')
        self.profesor = Profesor.objects.create(usuario=self.profesor_user, profesion='Ingeniero', centro_laboral='Universidad de Lima')

    def test_crear_curso(self):
        curso = Curso.objects.create(
            nombre='Matemáticas',
            descripcion='Curso de matemáticas avanzadas',
            categoria='Desarrollo',
            nivel='Intermedio',
            profesor=self.profesor
        )
        self.assertEqual(curso.nombre, 'Matemáticas')
        self.assertEqual(curso.profesor.usuario.nombre, 'Luis')
        self.assertEqual(curso.calificacion_promedio, 0)

    def test_actualizar_calificacion_promedio(self):
        curso = Curso.objects.create(
            nombre='Matemáticas',
            descripcion='Curso de matemáticas avanzadas',
            categoria='Desarrollo',
            nivel='Intermedio',
            profesor=self.profesor
        )
        curso.actualizar_calificacion_promedio()
        self.assertEqual(curso.calificacion_promedio, 0)
