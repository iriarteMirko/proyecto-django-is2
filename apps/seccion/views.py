from django.shortcuts import render
from rest_framework import viewsets
from .serializer import SeccionSerializer
from .models import Seccion

class SeccionViewSet(viewsets.ModelViewSet):
    serializer_class = SeccionSerializer
    queryset = Seccion.objects.all()