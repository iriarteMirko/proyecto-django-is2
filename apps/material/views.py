from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Material
from apps.curso.models import Seccion

def agregar_material(request, seccion_id):
    seccion = get_object_or_404(Seccion, id=seccion_id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        archivo = request.FILES.get('archivo')
        if nombre and archivo:
            Material.objects.create(nombre=nombre, archivo=archivo, seccion=seccion)
            return redirect('contenido_curso', curso_id=seccion.curso.id, curso_nombre=seccion.curso.nombre)
    return render(request, 'material/agregar_material.html', {'seccion': seccion})

def eliminar_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    curso_id = material.seccion.curso.id
    curso_nombre = material.seccion.curso.nombre
    material.delete()
    return redirect('contenido_curso', curso_id=curso_id, curso_nombre=curso_nombre)
