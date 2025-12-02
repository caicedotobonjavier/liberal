from django.shortcuts import render
#
from .models import User
#
from .forms import UserForm
#
from django.views.generic import FormView
#
from django.urls import reverse_lazy
# Create your views here.


class CreateUserView(FormView):
    template_name = 'users/crear-usuario.html'
    form_class = UserForm
    success_url = reverse_lazy('users_app:nuevo_usuario')


    def form_valid(self, form):
        email = form.cleaned_data['email']
        nombre_completo = form.cleaned_data['nombre_completo']
        password = form.cleaned_data['password']
        direccion = form.cleaned_data['direccion']
        telefono = form.cleaned_data['telefono']
        fecha_nacimiento = form.cleaned_data['fecha_nacimiento']

        User.objects.create_user(
            email,
            nombre_completo,
            password,
            direccion = direccion,
            telefono = telefono,
            fecha_nacimiento = fecha_nacimiento
        )

        return super(CreateUserView, self).form_valid(form)