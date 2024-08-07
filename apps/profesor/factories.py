from abc import ABC, abstractmethod
from apps.curso.models import Curso
from apps.seccion.models import Seccion
from apps.asesoria.models import Asesoria

class CursoFactory(ABC):
    @abstractmethod
    def create_curso(self, nombre, descripcion, categoria, nivel, profesor):
        pass
    
    @abstractmethod
    def create_seccion(self, curso, nombre, descripcion):
        pass

class CursoConcreteFactory(CursoFactory):
    def create_curso(self, nombre, descripcion, categoria, nivel, profesor):
        curso = Curso.objects.create(nombre=nombre, descripcion=descripcion, categoria=categoria, nivel=nivel, profesor=profesor)
        return curso
    
    def create_seccion(self, curso, nombre, descripcion):
        seccion = Seccion.objects.create(curso=curso, nombre=nombre, descripcion=descripcion)
        return seccion
    
    def create_asesoria(self, curso, fecha, hora_inicio, hora_fin, enlace):
        asesoria = Asesoria.objects.create(curso=curso, fecha=fecha, hora_inicio=hora_inicio, hora_fin=hora_fin, enlace=enlace)
        return asesoria
