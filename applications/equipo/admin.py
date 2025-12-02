from django.contrib import admin
#
from .models import Equipo
# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'cargo',
        'descripcion',
        'foto',
        'correo',
        'telefono',
        'visible',
    )

admin.site.register(Equipo, EquipoAdmin)
