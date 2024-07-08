# apps/seccion/tests.py
from django.test import TestCase
from apps.curso.models import Curso
from apps.profesor.models import Profesor
from .models import Seccion
from django.contrib.auth import get_user_model

class SeccionModelTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.profesor_user = User.objects.create_user(codigo='20191629', email='profesor@ulima.edu.pe', nombre='Luis', apellidos='Pérez', password='profesor123')
        self.profesor = Profesor.objects.create(usuario=self.profesor_user, profesion='Ingeniero', centro_laboral='Universidad de Lima')
        self.curso = Curso.objects.create(
            nombre='Matemáticas',
            descripcion='Curso de matemáticas avanzadas',
            categoria='Desarrollo',
            nivel='Intermedio',
            profesor=self.profesor
        )

    def test_crear_seccion(self):
        seccion = Seccion.objects.create(
            curso=self.curso,
            nombre='Algebra',
            descripcion='Sección de algebra avanzada'
        )
        self.assertEqual(seccion.curso.nombre, 'Matemáticas')
        self.assertEqual(seccion.nombre, 'Algebra')
