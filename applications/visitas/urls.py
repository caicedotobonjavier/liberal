from django.urls import path, include, re_path

from . import views

app_name = 'visitas_app'

urlpatterns = [
    path('visitas', views.VisitaView.as_view(), name='visitas'),
    path('detalle-visitas/<pk>/', views.DetalleVisitaView.as_view(), name='detalle-visitas'),
]
