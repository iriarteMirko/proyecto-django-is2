from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    path('usuario/', include('usuario.urls')),
    path('', include('estudiante.urls')),
    path('estudiante/', include('estudiante.urls')),
    path('', include('profesor.urls')),
    path('profesor/', include('profesor.urls')),
    path('', include('curso.urls')),
    path('curso/', include('curso.urls')),
    path('', include('seccion.urls')),
    path('seccion/', include('seccion.urls')),
    path('', include('inscripcion.urls')),
    path('inscripcion/', include('inscripcion.urls')),
    path('', include('calificacion.urls')),
    path('calificacion/', include('calificacion.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)