# apps/estudiante/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Estudiante

class EstudianteModelTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(codigo='20191627', email='20191627@aloe.ulima.edu.pe', nombre='Juan', apellidos='Gutiérrez', password='Elpapi12')
    
    def test_crear_estudiante(self):
        estudiante = Estudiante.objects.create(
            usuario=self.user,
            carrera='Comunicación',
            ciclo=9
        )
        self.assertEqual(estudiante.usuario.codigo, '20191627')
        self.assertEqual(estudiante.carrera, 'Comunicación')
        self.assertEqual(estudiante.ciclo, 9)

    def test_estudiante_str(self):
        estudiante = Estudiante.objects.create(
            usuario=self.user,
            carrera='Comunicación',
            ciclo=9
        )
        self.assertEqual(str(estudiante), 'Juan Gutiérrez')

    def test_estudiante_profesor_validacion(self):
        self.user.es_profesor = True
        self.user.save()
        with self.assertRaises(ValidationError):
            estudiante = Estudiante.objects.create(
                usuario=self.user,
                carrera='Comunicación',
                ciclo=9
            )
            estudiante.clean()
