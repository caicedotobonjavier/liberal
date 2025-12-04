from django.db import models
#
from model_utils.models import TimeStampedModel
#
from applications.municipios.models import Municipio
#
from ckeditor_uploader.fields import RichTextUploadingField

from cloudinary.models import CloudinaryField  # <-- NUEVA IMPORTACIÓN
# Create your models here.

class Visita(TimeStampedModel):
    titulo = models.CharField('Titulo Visita', max_length=100)
    municipio = models.ForeignKey(Municipio, related_name='municipio_visita', on_delete=models.CASCADE)
    fecha_visita = models.DateField('Fecha Visita', auto_now=False, auto_now_add=False)
    resumen = models.TextField('Resumen')
    contenido = RichTextUploadingField('Contenido')
    imagen_principal = CloudinaryField('imagen', folder='visita/')
    fecha_publicado = models.DateField('Fecha Publicacion', auto_now=False, auto_now_add=False)
    publicado = models.BooleanField('Publicado', default=False)


    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'
        ordering = ['id']
    

    def __str__(self):
        return self.titulo


class FotoVisita(TimeStampedModel):
    visita = models.ForeignKey(Visita, related_name='fotovisita_visita', on_delete=models.CASCADE)
    imagen = CloudinaryField('imagen', folder='visita/galeria')
    descripcion = models.CharField('Descripcion', max_length=100)

    class Meta:
        verbose_name = 'Foto Visita'
        verbose_name_plural = 'Fotos Visitas'
        ordering = ['id']
    

    def __str__(self):
        return self.visita.titulo