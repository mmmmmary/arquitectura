from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import base, register_view, productos_destacados, agregar_al_carrito, ver_carrito, eliminar_item_carrito  # Importa las vistas necesarias

app_name = 'myapp'  # Nombre de la aplicación

urlpatterns = [
    path('', productos_destacados, name='productos_destacados'),  # Ruta para mostrar los productos
    path('base/', base, name='base'),  # Si es necesario mantener la vista base
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Vista genérica de login
    path('carrito/', ver_carrito, name='ver_carrito'),  # Ruta para ver el carrito
    path('carrito/agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),  # Ruta para agregar productos al carrito
    path('carrito/eliminar/<int:item_id>/', eliminar_item_carrito, name='eliminar_item_carrito'),  # Ruta para eliminar ítems del carrito
    path('logout/', LogoutView.as_view(next_page='myapp:base'), name='logout'),  # Ruta para cerrar sesión y redirigir a base
]
