from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from apps.usuario.models import Usuario
from apps.estudiante.models import Estudiante

class EstudianteTests(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(
            codigo='20230004',
            email='estudiante@example.com',
            password='12345',
            nombre='Estudiante',
            apellidos='Prueba',
            es_estudiante=True
        )
        self.estudiante = Estudiante.objects.create(usuario=self.user, carrera='Ingeniería de Sistemas', ciclo=5)
    
    def test_estudiante_registro(self):
        self.assertEqual(self.estudiante.usuario, self.user)
        self.assertEqual(self.estudiante.carrera, 'Ingeniería de Sistemas')
        self.assertEqual(self.estudiante.ciclo, 5)
    
    def test_estudiante_clean_method(self):
        profesor_user = Usuario.objects.create_user(
            codigo='20230005',
            email='profesor@example.com',
            password='12345',
            nombre='Profesor',
            apellidos='Prueba',
            es_profesor=True
        )
        with self.assertRaisesMessage(ValidationError, "El usuario no puede ser estudiante y profesor al mismo tiempo."):
            estudiante = Estudiante(usuario=profesor_user, carrera='Arquitectura', ciclo=2)
            estudiante.clean()