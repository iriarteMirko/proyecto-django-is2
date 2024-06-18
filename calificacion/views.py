from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import CalificacionSerializer
from .models import Calificacion
from curso.models import Curso
from estudiante.models import Estudiante

class CalificacionViewSet(viewsets.ModelViewSet):
    serializer_class = CalificacionSerializer
    queryset = Calificacion.objects.all()

@login_required
def calificar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    estudiante = request.user.estudiante
    if request.method == 'POST':
        calificacion_valor = int(request.POST.get('calificacion'))
        calificacion, created = Calificacion.objects.update_or_create(
            curso=curso,
            estudiante=estudiante,
            defaults={'calificacion': calificacion_valor},
        )
        curso.actualizar_calificacion_promedio()
        return redirect('detalle_curso', curso_id=curso.id)
    return render(request, 'calificacion/calificar_curso.html', {'curso': curso})
