from abc import ABC, abstractmethod
from curso.models import Curso

class CursoFactory(ABC):
    @abstractmethod
    def create_curso(self, nombre, descripcion, profesor):
        pass

class CursoConcreteFactory(CursoFactory):
    def create_curso(self, nombre, descripcion, profesor):
        curso = Curso.objects.create(nombre=nombre, descripcion=descripcion, profesor=profesor)
        return curso
