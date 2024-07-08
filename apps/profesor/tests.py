# apps/profesor/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Profesor

class ProfesorModelTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            codigo='20191629', 
            email='profesor@ulima.edu.pe', 
            nombre='Luis', 
            apellidos='Pérez', 
            password='profesor123'
        )

    def test_crear_profesor(self):
        profesor = Profesor.objects.create(
            usuario=self.user,
            profesion='Ingeniero',
            centro_laboral='Universidad de Lima'
        )
        self.assertEqual(profesor.usuario.codigo, '20191629')
        self.assertEqual(profesor.profesion, 'Ingeniero')

    def test_profesor_clean_method(self):
        self.user.es_estudiante = True
        self.user.save()
        with self.assertRaises(ValidationError):
            profesor = Profesor.objects.create(
                usuario=self.user,
                profesion='Ingeniero',
                centro_laboral='Universidad de Lima'
            )
            profesor.clean()
