from django.test import TestCase
from django.urls import reverse
from apps.usuario.models import Usuario
from apps.curso.models import Curso
from apps.seccion.models import Seccion
from apps.profesor.models import Profesor

class SeccionTests(TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        self.user = Usuario.objects.create_user(
            codigo='20230001',
            email='testuser@example.com',
            password='12345',
            nombre='Test',
            apellidos='User',
            es_profesor=True
        )
        self.profesor = Profesor.objects.create(usuario=self.user, profesion='Ingeniero', centro_laboral='Universidad')
        self.curso = Curso.objects.create(
            nombre='Curso de Prueba',
            descripcion='Descripción del curso',
            categoria='Desarrollo',
            nivel='Intermedio',
            profesor=self.profesor
        )
        self.seccion = Seccion.objects.create(curso=self.curso, nombre='Sección de Prueba', descripcion='Descripción de la sección')
    
    def test_editar_seccion(self):
        self.client.login(codigo='20230001', password='12345')
        response = self.client.post(reverse('editar_seccion', args=[self.seccion.id]), {
            'nombre': 'Sección Editada',
            'descripcion': 'Descripción editada de la sección',
        })
        self.seccion.refresh_from_db()
        self.assertEqual(self.seccion.nombre, 'Sección Editada')
        self.assertEqual(self.seccion.descripcion, 'Descripción editada de la sección')
        self.assertRedirects(response, reverse('contenido_curso', args=[self.curso.id, self.curso.slug]))
    
    def test_eliminar_seccion(self):
        self.client.login(codigo='20230001', password='12345')
        response = self.client.post(reverse('eliminar_seccion', args=[self.seccion.id]))
        self.assertFalse(Seccion.objects.filter(id=self.seccion.id).exists())
        self.assertRedirects(response, reverse('contenido_curso', args=[self.curso.id, self.curso.slug]))