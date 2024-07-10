from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import MaterialSerializer
from .models import Material
from .forms import MaterialForm
from apps.seccion.models import Seccion
from apps.usuario.decorators import VistaBase, ProfesorDecorator

class MaterialViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()

class AgregarMaterialVista(VistaBase):
    def procesar_solicitud(self, request, seccion_id, *args, **kwargs):
        seccion = get_object_or_404(Seccion, id=seccion_id)
        if request.method == 'POST':
            form = MaterialForm(request.POST, request.FILES)
            if form.is_valid():
                material = form.save(commit=False)
                material.seccion = seccion
                material.save()
        return redirect('contenido_curso', curso_id=seccion.curso.id, curso_slug=seccion.curso.slug)

class EliminarMaterialVista(VistaBase):
    def procesar_solicitud(self, request, material_id, *args, **kwargs):
        material = get_object_or_404(Material, id=material_id)
        curso_id = material.seccion.curso.id
        curso_slug = material.seccion.curso.slug
        material.delete()
        return redirect('contenido_curso', curso_id=curso_id, curso_slug=curso_slug)

@login_required
def agregar_material(request, seccion_id):
    vista = AgregarMaterialVista()
    vistaDecorada = ProfesorDecorator(vista)
    return vistaDecorada.procesar_solicitud(request, seccion_id)

@login_required
def eliminar_material(request, material_id):
    vista = EliminarMaterialVista()
    vistaDecorada = ProfesorDecorator(vista)
    return vistaDecorada.procesar_solicitud(request, material_id)