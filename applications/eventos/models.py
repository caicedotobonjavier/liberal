from django.db import models
#
from model_utils.models import TimeStampedModel
# Create your models here.

class Evento(TimeStampedModel):
    titulo = models.CharField('Titulo Evento', max_length=100)
    fecha_evento = models.DateTimeField('Fecha Evento', auto_now=False, auto_now_add=False)
    lugar = models.CharField('Lugar Evento', max_length=50)
    descripcion = models.TextField('Descripcion Evento')
    publicado = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['id']
    

    def __str__(self):
        return self.titulo

