from django.urls import path

from . import views

app_name = 'users_app'


urlpatterns = [
    path('crear-usuario', views.CreateUserView.as_view(), name='nuevo_usuario'),
]
