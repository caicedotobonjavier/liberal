from django.contrib import admin
#
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "nombre_completo",
        "direccion",
        "telefono",
        "fecha_nacimiento",
        "codigo_registro",
        "is_superuser",
        "is_active",
        "is_staff",
    )


admin.site.register(User, UserAdmin)