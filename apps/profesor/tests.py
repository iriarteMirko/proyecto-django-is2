from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from apps.usuario.models import Usuario
from apps.profesor.models import Profesor

class ProfesorTests(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(
            codigo='20230002',
            email='profesor@example.com',
            password='12345',
            nombre='Profesor',
            apellidos='Prueba',
            es_profesor=True
        )
        self.profesor = Profesor.objects.create(usuario=self.user, profesion='Ingeniero', centro_laboral='Universidad')
    
    def test_profesor_registro(self):
        self.assertEqual(self.profesor.usuario, self.user)
        self.assertEqual(self.profesor.profesion, 'Ingeniero')
        self.assertEqual(self.profesor.centro_laboral, 'Universidad')
    
    def test_profesor_clean_method(self):
        estudiante_user = Usuario.objects.create_user(
            codigo='20230003',
            email='estudiante@example.com',
            password='12345',
            nombre='Estudiante',
            apellidos='Prueba',
            es_estudiante=True
        )
        with self.assertRaisesMessage(ValidationError, "El usuario no puede ser profesor y estudiante al mismo tiempo."):
            profesor = Profesor(usuario=estudiante_user, profesion='Doctor', centro_laboral='Hospital')
            profesor.clean()