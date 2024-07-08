from django.core.management.base import BaseCommand
from django.utils.text import slugify
from curso.models import Curso

class Command(BaseCommand):
    help = 'Genera slugs para cursos existentes'
    
    def handle(self, *args, **kwargs):
        cursos = Curso.objects.all()
        for curso in cursos:
            if not curso.slug:
                curso.slug = slugify(curso.nombre)
                curso.save()
        self.stdout.write(self.style.SUCCESS('Slugs generados para cursos.'))