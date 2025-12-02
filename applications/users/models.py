from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from django.db.models.signals import pre_save
#
from .managers import UserManager
#
from .functions import crear_codigo
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    nombre_completo = models.CharField('Nombre Completo', max_length=100)
    direccion = models.CharField('Direccion', max_length=50, null=True, blank=True)
    telefono = models.CharField('Telefono', max_length=20, null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha Nacimiento', auto_now=False, auto_now_add=False, null=True, blank=True)
    codigo_registro = models.CharField('Codigo Registro', max_length=6, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['nombre_completo']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
    
    
def asignar_codigo(sender, instance, **kwargs):
    instance.codigo_registro = crear_codigo()


pre_save.connect(asignar_codigo, sender=User)