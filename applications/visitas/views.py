#
from .models import Visita, FotoVisita
#
from django.views.generic import TemplateView, DetailView
#
from datetime import datetime

class VisitaView(TemplateView):
    template_name = 'visitas/visitas.html'


    def get_context_data(self, **kwargs):
        context = super(VisitaView, self).get_context_data(**kwargs)
        context["visitas"] = Visita.objects.filter(publicado=True).order_by('-fecha_publicado')
        context["now"] = datetime.now()
        return context


class DetalleVisitaView(DetailView):
    template_name = 'visitas/detalle-visita.html'
    
    def get_queryset(self):
        return Visita.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_fotos = self.kwargs['pk']
        context["fotos"] = FotoVisita.objects.filter(visita_id = id_fotos).all()
        context["now"] = datetime.now()        
        return context
    