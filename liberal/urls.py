"""
URL configuration for liberal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path, include, re_path
#from django.conf import settings
#from django.conf.urls.static import static
#
#urlpatterns = [
#    path('admin/', admin.site.urls),
#    re_path('', include('applications.users.urls')),
#    re_path('', include('applications.home.urls')),
#    re_path('', include('applications.visitas.urls')),
#    re_path('', include('applications.eventos.urls')),
#    re_path('', include('applications.contacto.urls')),
#    re_path('', include('applications.equipo.urls')),
#    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
#]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.http import JsonResponse
import os

def debug_cloudinary(request):
    return JsonResponse({
        'status': 'ok',
        'debug': settings.DEBUG,
    })

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.visitas.urls')),
    re_path('', include('applications.eventos.urls')),
    re_path('', include('applications.contacto.urls')),
    re_path('', include('applications.equipo.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# Solo para DEBUG, pero no te causa problema en prod
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# IMPORTANTE: Mantén esta línea PERO solo para desarrollo
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
