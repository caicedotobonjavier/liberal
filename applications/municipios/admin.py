from django.contrib import admin
#
from .models import Municipio
# Register your models here.

class MunicipioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'departamento',
        'descripcion',
    )

admin.site.register(Municipio, MunicipioAdmin)