from django.db import models
#
from model_utils.models import TimeStampedModel
#
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Equipo(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=150)
    cargo = models.CharField('Cargo', max_length=150)
    descripcion = RichTextUploadingField('Descripcion')
    foto = models.ImageField('Foto', upload_to="equipo/", blank=True, null=True)
    correo = models.EmailField('Correo Contacto', blank=True, null=True)
    telefono = models.CharField('Telefono', max_length=20, blank=True)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Persona del Equipo'
        verbose_name_plural = 'Personas del Equipo'
        ordering = ["cargo", "nombre"]

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"