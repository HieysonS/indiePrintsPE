from django.http import HttpResponse
from django.shortcuts import render

from producto.models import Producto


# Create your views here.


def inicio(request):
    numeroProductos = Producto.objects.count()
    productos = Producto.objects.all()
    return render(request, 'inicio.html', {'nproductos': numeroProductos, 'productos': productos})

# def despedida(request):
#   return HttpResponse('Bye...!')
