from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CursoSerializer
from .models import Curso

class CursoViewSet(viewsets.ModelViewSet):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()