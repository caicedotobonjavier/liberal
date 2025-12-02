from django.urls import path, include, re_path

from . import views

app_name = 'contacto_app'

urlpatterns = [
    path('contacto', views.ContactoView.as_view(), name='contactos'),
    path('contacto-exitoso', views.ContactoExitosoView.as_view(), name='contacto-exitoso'),
]
