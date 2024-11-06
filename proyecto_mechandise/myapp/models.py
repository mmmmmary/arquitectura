# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

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