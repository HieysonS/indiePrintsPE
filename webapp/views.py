from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from producto.models import Producto


# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def contacto(request):
    return render(request, 'paginas/contacto.html')


@login_required
def administrar(request):
    return render(request, 'paginas/administrar.html')


def salir(request):
    logout(request)
    return redirect('/')


def catalogo(request):
    categoria = request.GET.get('categoria')
    if categoria:
        productos_list = Producto.objects.filter(categoria=categoria)
    else:
        productos_list = Producto.objects.all()

    paginator = Paginator(productos_list, 3)  # Muestra 3 productos por página

    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)

    return render(request, 'catalogo.html', {'productos': productos})


def detalleProducto(request, id):
    # producto = Producto.objects.get(pk=id)
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'detalleProducto.html', {'producto': producto})
