from django.db import models
#
from model_utils.models import TimeStampedModel
#
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Contacto(TimeStampedModel):
    nombre_completo = models.CharField('Nombre', max_length=100)
    email = models.EmailField('Correo Electronico', max_length=254)
    telefono = models.CharField('Telefono', max_length=50)
    asunto = models.CharField('Asunto', max_length=50)
    mensaje = RichTextUploadingField('Mensaje')
    fecha = models.DateTimeField('Fecha', auto_now_add=True)
    leido = models.BooleanField('Mensaje Leido', default=False)


    class Meta:
        verbose_name = 'Mensaje de Contacto'
        verbose_name_plural = 'Mensajes de Contato'
        ordering = ['fecha']
    

    def __str__(self):
        return self.nombre_completo
    
