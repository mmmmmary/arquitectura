# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['nombre', 'apellido_paterno', 'direccion_calle', 'comuna', 'region', 'pais', 'rut', 'username', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  # Agrega la clase CSS a cada campo

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if CustomUser.objects.filter(rut=rut).exists():
            raise forms.ValidationError("El RUT ya está en uso.")
        return rut
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya existe.")
        return username
