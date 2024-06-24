from abc import ABC, abstractmethod
from curso.models import Curso
from seccion.models import Seccion

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
