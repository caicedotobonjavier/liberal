from django.shortcuts import render
#
from django.views.generic import TemplateView
#
from .models import Equipo
#
from datetime import datetime
# Create your views here.

class EquipoView(TemplateView):
    template_name = 'equipo/equipo.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = Equipo.objects.all().order_by('id')
        context["now"] = datetime.now()
        return context
    
