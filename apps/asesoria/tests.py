# apps/asesoria/tests.py
from django.test import TestCase
from django.utils import timezone
from apps.curso.models import Curso
from apps.profesor.models import Profesor
from .models import Asesoria
from django.contrib.auth import get_user_model

class AsesoriaModelTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.profesor_user = User.objects.create_user(codigo='20191629', email='profesor@ulima.edu.pe', nombre='Luis', apellidos='Pérez', password='profesor123')
        self.profesor = Profesor.objects.create(usuario=self.profesor_user, profesion='Ingeniero', centro_laboral='Universidad de Lima')
        self.curso = Curso.objects.create(
            nombre='Matemáticas',
            descripcion='Curso de matemáticas avanzadas',
            categoria='Desarrollo',
            nivel='Intermedio',
            profesor=self.profesor
        )

    def test_crear_asesoria(self):
        fecha = timezone.now().date() + timezone.timedelta(days=1)
        hora_inicio = timezone.now().time().replace(hour=14, minute=0, second=0, microsecond=0)
        hora_fin = timezone.now().time().replace(hour=15, minute=0, second=0, microsecond=0)
        asesoria = Asesoria.objects.create(
            curso=self.curso,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            enlace='http://reunion.zoom/123456'
        )
        self.assertEqual(asesoria.curso.nombre, 'Matemáticas')
        self.assertEqual(asesoria.fecha, fecha)
        self.assertEqual(asesoria.hora_inicio, hora_inicio)
        self.assertEqual(asesoria.hora_fin, hora_fin)
