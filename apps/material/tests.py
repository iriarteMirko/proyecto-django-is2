from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.profesor.models import Profesor
from apps.curso.models import Curso
from apps.seccion.models import Seccion
from .models import Material
import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()

class MaterialTestCase(TestCase):
    def setUp(self):
        # Set up a temporary file to act as the material file
        self.temp_file = tempfile.NamedTemporaryFile(suffix=".txt")
        self.temp_file.write(b"Test file content")
        self.temp_file.seek(0)
        
        # Create a test user, professor, course, and section
        self.user = User.objects.create_user(username='testuser', password='12345', es_profesor=True)
        self.profesor = Profesor.objects.create(usuario=self.user)
        self.curso = Curso.objects.create(
            nombre='Test Curso',
            descripcion='Descripción del curso de prueba',
            categoria='Desarrollo',
            nivel='Principiante',
            profesor=self.profesor,
            slug='test-curso'
        )
        self.seccion = Seccion.objects.create(
            curso=self.curso,
            nombre='Test Seccion',
            descripcion='Descripción de la sección de prueba'
        )
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_agregar_material(self):
        # Create a simple uploaded file for testing
        material_file = SimpleUploadedFile(self.temp_file.name, self.temp_file.read(), content_type='text/plain')

        response = self.client.post(reverse('agregar_material', kwargs={'seccion_id': self.seccion.id}), {
            'nombre': 'Test Material',
            'archivo': material_file
        })

        self.assertEqual(response.status_code, 302)  # Redirection after successful creation
        self.assertTrue(Material.objects.filter(nombre='Test Material').exists())

    def test_eliminar_material(self):
        # Create a material instance
        material = Material.objects.create(
            seccion=self.seccion,
            nombre='Material para Eliminar',
            archivo=SimpleUploadedFile(self.temp_file.name, self.temp_file.read(), content_type='text/plain')
        )

        response = self.client.post(reverse('eliminar_material', kwargs={'material_id': material.id}))

        self.assertEqual(response.status_code, 302)  # Redirection after successful deletion
        self.assertFalse(Material.objects.filter(nombre='Material para Eliminar').exists())