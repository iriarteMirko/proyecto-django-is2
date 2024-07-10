from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.usuario.urls')),
    path('usuario/', include('apps.usuario.urls')),
    path('', include('apps.estudiante.urls')),
    path('estudiante/', include('apps.estudiante.urls')),
    path('', include('apps.profesor.urls')),
    path('profesor/', include('apps.profesor.urls')),
    path('', include('apps.curso.urls')),
    path('curso/', include('apps.curso.urls')),
    path('', include('apps.seccion.urls')),
    path('seccion/', include('apps.seccion.urls')),
    path('', include('apps.asesoria.urls')),
    path('asesoria/', include('apps.asesoria.urls')),
    path('', include('apps.inscripcion.urls')),
    path('inscripcion/', include('apps.inscripcion.urls')),
    path('', include('apps.material.urls')),
    path('material/', include('apps.material.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuración de la vista personalizada para errores 404
handler404 = 'apps.usuario.views.error_404_view'