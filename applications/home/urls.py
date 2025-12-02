from django.urls import path, include, re_path

from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
]