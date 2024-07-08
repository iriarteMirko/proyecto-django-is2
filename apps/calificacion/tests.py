# apps/calificacion/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.profesor.models import Profesor
from apps.curso.models import Curso
from apps.estudiante.models import Estudiante
from apps.inscripcion.models import Inscripcion
from .models import Calificacion

class CalificacionModelTests(TestCase):

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
        self.inscripcion = Inscripcion.objects.create(
            curso=self.curso,
            estudiante=self.estudiante
        )

    def test_crear_calificacion(self):
        calificacion = Calificacion.objects.create(
            curso=self.curso,
            estudiante=self.estudiante,
            calificacion=5
        )
        self.assertEqual(calificacion.curso.nombre, 'Matemáticas')
        self.assertEqual(calificacion.estudiante.usuario.nombre, 'Juan')
        self.assertEqual(calificacion.calificacion, 5)

    def test_calificacion_sin_inscripcion(self):
        self.inscripcion.delete()
        with self.assertRaises(ValueError):
            Calificacion.objects.create(
                curso=self.curso,
                estudiante=self.estudiante,
                calificacion=5
            )
