from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import SeccionSerializer
from .form import SeccionForm
from .models import Seccion

class SeccionViewSet(viewsets.ModelViewSet):
    serializer_class = SeccionSerializer
    queryset = Seccion.objects.all()

@login_required
def editar_seccion(request, seccion_id):
    seccion = Seccion.objects.get(id=seccion_id)
    if request.method == 'POST':
        form = SeccionForm(request.POST, instance=seccion)
        if form.is_valid():
            form.save()
            return redirect('contenido_curso', curso_id=seccion.curso.id, curso_nombre=seccion.curso.nombre)
    else:
        form = SeccionForm(instance=seccion)
    return render(request, 'seccion/editar_seccion.html', {'form': form, 'seccion': seccion})

@login_required
def eliminar_seccion(request, seccion_id):
    seccion = Seccion.objects.get(id=seccion_id)
    seccion.delete()
    return redirect('contenido_curso', curso_id=seccion.curso.id, curso_nombre=seccion.curso.nombre)