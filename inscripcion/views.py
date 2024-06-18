from django.shortcuts import render
from rest_framework import viewsets
from .serializer import InscripcionSerializer
from .models import Inscripcion

class InscripcionViewSet(viewsets.ModelViewSet):
    serializer_class = InscripcionSerializer
    queryset = Inscripcion.objects.all()