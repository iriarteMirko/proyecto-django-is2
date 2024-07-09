from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from apps.curso.models import Curso
from apps.profesor.models import Profesor
from apps.usuario.models import Usuario
from .models import Asesoria

class AsesoriaModelTests(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(
            codigo='20191629',
            email='profesor@ulima.edu.pe',
            nombre='Luis',
            apellidos='Pérez',
            password='profesor123',
            es_profesor=True
        )
        self.profesor = Profesor.objects.create(usuario=self.user, profesion='Ingeniero', centro_laboral='Universidad de Lima')
        self.curso = Curso.objects.create(
            nombre='Matemáticas',
            descripcion='Curso de matemáticas avanzadas',
            categoria='Desarrollo',
            nivel='Intermedio',
            profesor=self.profesor
        )
        self.fecha = timezone.now().date() + timezone.timedelta(days=1)
        self.hora_inicio = timezone.now().time().replace(hour=14, minute=0, second=0, microsecond=0)
        self.hora_fin = timezone.now().time().replace(hour=15, minute=0, second=0, microsecond=0)
        self.asesoria = Asesoria.objects.create(
            curso=self.curso,
            fecha=self.fecha,
            hora_inicio=self.hora_inicio,
            hora_fin=self.hora_fin,
            enlace='http://reunion.zoom/123456'
        )

    def test_crear_asesoria(self):
        self.assertEqual(self.asesoria.curso.nombre, 'Matemáticas')
        self.assertEqual(self.asesoria.fecha, self.fecha)
        self.assertEqual(self.asesoria.hora_inicio, self.hora_inicio)
        self.assertEqual(self.asesoria.hora_fin, self.hora_fin)
        self.assertEqual(self.asesoria.enlace, 'http://reunion.zoom/123456')

    def test_editar_asesoria(self):
        self.client.login(codigo='20191629', password='profesor123')
        nueva_fecha = self.fecha + timezone.timedelta(days=2)
        nueva_hora_inicio = self.hora_inicio.replace(hour=16, minute=0, second=0)
        nueva_hora_fin = self.hora_fin.replace(hour=17, minute=0, second=0)
        response = self.client.post(reverse('editar_asesoria', args=[self.asesoria.id]), {
            'fecha': nueva_fecha.strftime('%Y-%m-%d'),
            'hora_inicio': nueva_hora_inicio.strftime('%H:%M'),
            'hora_fin': nueva_hora_fin.strftime('%H:%M'),
            'enlace': 'http://reunion.zoom/789012'
        })
        self.asesoria.refresh_from_db()
        self.assertEqual(self.asesoria.fecha, nueva_fecha)
        self.assertEqual(self.asesoria.hora_inicio, nueva_hora_inicio)
        self.assertEqual(self.asesoria.hora_fin, nueva_hora_fin)
        self.assertEqual(self.asesoria.enlace, 'http://reunion.zoom/789012')
        self.assertRedirects(response, reverse('asesoria_curso', args=[self.curso.id, self.curso.slug]))

    def test_eliminar_asesoria(self):
        self.client.login(codigo='20191629', password='profesor123')
        response = self.client.post(reverse('eliminar_asesoria', args=[self.asesoria.id]))
        self.assertFalse(Asesoria.objects.filter(id=self.asesoria.id).exists())
        self.assertRedirects(response, reverse('asesoria_curso', args=[self.curso.id, self.curso.slug]))