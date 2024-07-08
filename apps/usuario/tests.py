# apps/usuario/tests.py
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Usuario

class UsuarioModelTests(TestCase):

    def test_crear_usuario(self):
        user = Usuario.objects.create_user(
            codigo='20191627',
            email='20191627@aloe.ulima.edu.pe',
            nombre='Juan',
            apellidos='Gutiérrez',
            password='Elpapi12'
        )
        self.assertEqual(user.codigo, '20191627')
        self.assertTrue(user.check_password('Elpapi12'))

    def test_usuario_clean_method(self):
        user = Usuario.objects.create_user(
            codigo='20191628',
            email='20191628@aloe.ulima.edu.pe',
            nombre='María',
            apellidos='López',
            password='password123',
            es_estudiante=True,
            es_profesor=True
        )
        with self.assertRaises(ValidationError):
            user.clean()
