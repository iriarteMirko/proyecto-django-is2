from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import AsesoriaSerializer
from .models import Asesoria
from apps.curso.models import Curso
from apps.estudiante.models import Estudiante


class AsesoriaViewSet(viewsets.ModelViewSet):
    serializer_class = AsesoriaSerializer
    queryset = Asesoria.objects.all()

