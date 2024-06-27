from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import CalificacionSerializer
from .models import Calificacion
from apps.curso.models import Curso
from apps.estudiante.models import Estudiante

class CalificacionViewSet(viewsets.ModelViewSet):
    serializer_class = CalificacionSerializer
    queryset = Calificacion.objects.all()