from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

import producto
from producto.models import Producto


# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def contacto(request):
    return render(request, 'paginas/contacto.html')


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
