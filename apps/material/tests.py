from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.profesor.models import Profesor
from apps.curso.models import Curso
from apps.seccion.models import Seccion
from apps.material.models import Material
import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()

class MaterialTestCase(TestCase):
    def setUp(self):
        # Creación material temporal para pruebas
        self.temp_file = tempfile.NamedTemporaryFile(suffix=".txt")
        self.temp_file.write(b"Test file content")
        self.temp_file.seek(0)
        # Creación de usuario
        self.user = User.objects.create_user(
            codigo='testcode',
            email='testuser@example.com',
            nombre='Test',
            apellidos='User',
            password='12345',
            es_profesor=True
        )
        # Creación de profesor
        self.profesor = Profesor.objects.create(
            usuario=self.user,
            profesion='Ingeniero de Software',
            centro_laboral='Universidad de Lima'
        )
        # Creación de curso
        self.curso = Curso.objects.create(
            nombre='Test Curso',
            descripcion='Descripción del curso de prueba',
            categoria='Desarrollo',
            nivel='Principiante',
            profesor=self.profesor,
            slug='test-curso'
        )
        # Creación de sección
        self.seccion = Seccion.objects.create(
            curso=self.curso,
            nombre='Test Seccion',
            descripcion='Descripción de la sección de prueba'
        )
        # Iniciar sesión
        self.client = Client()
        self.client.login(codigo='testcode', password='12345')
    
    def test_agregar_material(self):
        # Creación de un archivo simple para pruebas
        material_file = SimpleUploadedFile(self.temp_file.name, self.temp_file.read(), content_type='text/plain')
        response = self.client.post(reverse('agregar_material', kwargs={'seccion_id': self.seccion.id}), {
            'nombre': 'Test Material',
            'archivo': material_file
        })
        self.assertEqual(response.status_code, 302)  # Redirección después de la creación exitosa
        self.assertTrue(Material.objects.filter(nombre='Test Material').exists())
    
    def test_eliminar_material(self):
        # Creación de un material para eliminar
        material = Material.objects.create(
            seccion=self.seccion,
            nombre='Material para Eliminar',
            archivo=SimpleUploadedFile(self.temp_file.name, self.temp_file.read(), content_type='text/plain')
        )
        response = self.client.post(reverse('eliminar_material', kwargs={'material_id': material.id}))
        self.assertEqual(response.status_code, 302)  # Redirección después de la eliminación exitosa
        self.assertFalse(Material.objects.filter(nombre='Material para Eliminar').exists())