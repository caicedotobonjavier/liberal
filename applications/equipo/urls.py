from django.urls import path, include, re_path

from . import views

app_name = 'equipo_app'

urlpatterns = [
    path('equipo-trabajo', views.EquipoView.as_view(), name='equipo'),
]
