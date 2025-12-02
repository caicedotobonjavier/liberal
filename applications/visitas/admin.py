from django.contrib import admin
#
from .models import Visita, FotoVisita
# Register your models here.

class VisitaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'municipio',
        'fecha_visita',
        'resumen',
        'contenido',
        'imagen_principal',
        'fecha_publicado',
        'publicado',
    )

admin.site.register(Visita, VisitaAdmin)


class FotoVisitaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'visita',
        'imagen',
        'descripcion',
    )


admin.site.register(FotoVisita, FotoVisitaAdmin)