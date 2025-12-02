from django.urls import path, include, re_path

from . import views

app_name = 'eventos_app'

urlpatterns = [
    path('eventos', views.EventoView.as_view(), name='eventos'),
    path('detalle-eventos/<pk>/', views.DetalleEventoView.as_view(), name='detalle-eventos'),
]
