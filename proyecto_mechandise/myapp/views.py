from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Producto, Carrito, ItemCarrito

def base(request):
    context = {}
    return render(request, 'myapp/base.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cuenta creada con éxito!')
            return redirect('myapp:login')
        else:
            messages.error(request, 'Hubo un error al crear la cuenta. Por favor, verifica los campos.')
            print(form.errors)  # Imprime los errores en la consola
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '¡Has iniciado sesión con éxito!')
            return redirect('myapp:productos_destacados')  # Redirige a base.html o cualquier página principal
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def productos_destacados(request):
    productos = Producto.objects.all()  # Puedes filtrar si es necesario, por ejemplo, productos destacados
    return render(request, 'myapp/base.html', {'productos': productos})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    item, item_creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

    if not item_creado:
        item.cantidad += 1
    item.save()

    # Redirige al carrito después de agregar el producto
    return redirect('myapp:ver_carrito')

@login_required
def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    return render(request, 'myapp/carrito.html', {'carrito': carrito})

@login_required
def eliminar_item_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    item.delete()
    return redirect('myapp:ver_carrito')
