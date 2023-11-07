from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from producto.models import *


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
    categorias = Categoria.objects.order_by('nombreCategoria')
    colores = Color.objects.order_by('nombreColor')
    tallas = Talla.objects.order_by('nombreTalla')

    categoria = request.GET.get('categoria')
    color = request.GET.get('color')
    talla = request.GET.get('talla')
    busqueda = request.GET.get('busqueda')

    productos_list = Producto.objects.order_by('nombre')
    if categoria:
        productos_list = productos_list.filter(categoria=categoria)
    if color:
        productos_list = productos_list.filter(color=color)
    if talla:
        productos_list = productos_list.filter(talla=talla)
    if busqueda:
        productos_list = productos_list.filter(
            Q(nombre__icontains=busqueda) |
            Q(talla__nombreTalla__icontains=busqueda) |
            Q(material__nombreMaterial__icontains=busqueda) |
            Q(color__nombreColor__icontains=busqueda) |
            Q(categoria__nombreCategoria__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        )

    paginator = Paginator(productos_list, 3)  # Muestra 3 productos por página

    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)

    return render(request, 'catalogo.html', {'productos': productos, 'categorias': categorias, 'colores': colores, 'tallas': tallas})


def detalleProducto(request, id):
    # producto = Producto.objects.get(pk=id)
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'detalleProducto.html', {'producto': producto})
