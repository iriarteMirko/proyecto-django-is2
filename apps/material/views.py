from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import MaterialSerializer
from .models import Material
from apps.seccion.models import Seccion
from apps.usuario.decorators import VistaBase, ProfesorDecorator

class MaterialViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
