from django.shortcuts import render
#
from .models import Evento
#
from django.views.generic import TemplateView, DetailView
#
from datetime import datetime
# Create your views here.


class EventoView(TemplateView):
    template_name = 'eventos/eventos.html'

    def get_context_data(self, **kwargs):
        context = super(EventoView, self).get_context_data(**kwargs)
        context['eventos'] = Evento.objects.all().order_by('fecha_evento')
        context["now"] = datetime.now()
        return context


class DetalleEventoView(DetailView):
    template_name = 'eventos/detalle-evento.html'
    
    def get_queryset(self):
        evento_id = self.kwargs['pk']
        evento = Evento.objects.filter(id=evento_id)
        return evento

    def get_context_data(self, **kwargs):
        context = super(DetalleEventoView, self).get_context_data(**kwargs)
        context["now"] = datetime.now()
        return context
    