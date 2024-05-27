from django.contrib import admin
from django.urls import path, include

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
]
