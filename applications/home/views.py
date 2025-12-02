from django.shortcuts import render
#
from django.views.generic import TemplateView
#
from applications.visitas.models import Visita
#
from applications.eventos.models import Evento
#
from datetime import datetime
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/index.html'
    

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["visitas"] = Visita.objects.filter(publicado=True).order_by('-fecha_visita')[:3]
        context["eventos"] = Evento.objects.filter(publicado=True).order_by('fecha_evento')[:3]
        context["now"] = datetime.now()
        return context
    
    


