# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    direccion_calle = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, unique=True)

    # Especifica el related_name para evitar conflictos
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Cambia el nombre aquí
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Cambia el nombre aquí
        blank=True,
    )

    def __str__(self):
        return self.username

# Modelos para el carrito de compras
class Carrito(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
