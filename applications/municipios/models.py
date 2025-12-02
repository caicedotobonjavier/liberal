from django.db import models
#
from model_utils.models import TimeStampedModel
#
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Municipio(TimeStampedModel):

    DEPARTAMENTO_CHOICES = (
        ('1', 'Antioquia'),
    )

    nombre = models.CharField('Nombre Municipio', max_length=50)
    departamento = models.CharField('Departamento', max_length=1, choices=DEPARTAMENTO_CHOICES)
    descripcion = RichTextUploadingField('Descripcion')

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        ordering = ['id']
    

    def __str__(self):
        return self.nombre