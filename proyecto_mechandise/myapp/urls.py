from django.urls import path
from django.contrib.auth.views import LoginView
from .views import base, register_view  # Importa otras vistas si es necesario

app_name = 'myapp'  # Nombre de la aplicación

urlpatterns = [
    path('', base, name='base'),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Vista genérica de login
]
