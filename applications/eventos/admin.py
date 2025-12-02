from django.contrib import admin
#
from .models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'fecha_evento',
        'lugar',
        'descripcion',
        'publicado',
    )


admin.site.register(Evento, EventoAdmin)