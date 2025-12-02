from django.shortcuts import render
#
from .models import Contacto
#
from django.views.generic import FormView, TemplateView
#
from .forms import ContactoForm
#
from datetime import datetime
#
from django.urls import reverse_lazy
# Create your views here.


class ContactoExitosoView(TemplateView):
    template_name = 'contacto/contacto-exitoso.html'

    def get_context_data(self, **kwargs):
        context = super(ContactoExitosoView, self).get_context_data(**kwargs)
        context["now"] = datetime.now()
        return context


class ContactoView(FormView):
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto_app:contacto-exitoso')


    def get_context_data(self, **kwargs):
        context = super(ContactoView, self).get_context_data(**kwargs)
        context["now"] = datetime.now()
        return context
    

    def form_valid(self, form):
        nombre_completo = form.cleaned_data['nombre_completo']
        email = form.cleaned_data['email']
        telefono = form.cleaned_data['telefono']
        asunto = form.cleaned_data['asunto']
        mensaje = form.cleaned_data['mensaje']

        Contacto.objects.create(
            nombre_completo = nombre_completo,
            email = email,
            telefono = telefono,
            asunto = asunto,
            mensaje = mensaje,
        )

        return super(ContactoView, self).form_valid(form)
