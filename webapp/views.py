from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from producto.models import *

from django.shortcuts import get_object_or_404
from producto.views import Producto, Carrito, CarritoProducto


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
    materiales = Material.objects.order_by('nombreMaterial')

    categoria = request.GET.get('categoria')
    color = request.GET.get('color')
    talla = request.GET.get('talla')
    material = request.GET.get('material')
    busqueda = request.GET.get('busqueda')

    productos_list = Producto.objects.order_by('nombre')
    if categoria:
        productos_list = productos_list.filter(categoria=categoria)
    if color:
        productos_list = productos_list.filter(color=color)
    if material:
        productos_list = productos_list.filter(material=material)
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

    return render(request, 'catalogo.html',
                  {'productos': productos,
                   'categorias': categorias,
                   'colores': colores,
                   'tallas': tallas,
                   'materiales': materiales})


def detalleProducto(request, id):
    # producto = Producto.objects.get(pk=id)
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'detalleProducto.html', {'producto': producto})


def producto_a_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if producto.stock > 0:  # Verificar si hay stock
        carrito_id = request.session.get('carrito_id')
        if carrito_id:
            carrito = Carrito.objects.get(id=carrito_id)
        else:
            carrito = Carrito.objects.create()
            request.session['carrito_id'] = carrito.id
        CarritoProducto.objects.create(carrito=carrito, producto=producto, cantidad=1)
        producto.stock -= 1  # Disminuir el stock
        producto.save()
    return redirect("/catalogo")


def vaciar_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
        for item in carrito.carritoproducto_set.all():
            item.producto.stock += item.cantidad  # Devolver los productos al stock
            item.producto.save()
        carrito.carritoproducto_set.all().delete()
    return redirect("/mostrar_carrito")


def eliminar_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
        for item in carrito.carritoproducto_set.all():
            item.producto.stock += item.cantidad  # Devolver los productos al stock
            item.producto.save()
        Carrito.objects.filter(id=carrito_id).delete()
        del request.session['carrito_id']
    return redirect("/catalogo")


def aumentar_cantidad(request, producto_id):
    producto = get_object_or_404(CarritoProducto, id=producto_id)
    if producto.producto.stock > 0:  # Verificar si hay stock
        producto.cantidad += 1
        producto.producto.stock -= 1  # Disminuir el stock
        producto.producto.save()
        producto.save()
    return redirect("/mostrar_carrito")


def disminuir_cantidad(request, producto_id):
    producto = get_object_or_404(CarritoProducto, id=producto_id)
    producto.cantidad -= 1
    producto.producto.stock += 1  # Devolver el producto al stock
    producto.producto.save()
    if producto.cantidad == 0:
        producto.delete()
    else:
        producto.save()
    return redirect("/mostrar_carrito")


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(CarritoProducto, id=producto_id)
    producto.producto.stock += producto.cantidad  # Devolver los productos al stock
    producto.producto.save()
    producto.delete()
    return redirect("/mostrar_carrito")


def mostrar_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
        cantidad_total = sum(item.cantidad for item in carrito.carritoproducto_set.all())
    else:
        carrito = None
        cantidad_total = 0
    return render(request, 'carrito/carrito.html', {'carrito': carrito, 'cantidad_total': cantidad_total})


def detalles_carrito(request, carrito_id):
    carrito = Carrito.objects.get(id=carrito_id)
    return render(request, '/detalles_carrito/', {'carrito': carrito})


def crear_pedido(request):
    if request.method == 'POST':
        dni = request.POST['dni']
        nombre = request.POST['nombre']
        apellido_paterno = request.POST['apellido_paterno']
        apellido_materno = request.POST['apellido_materno']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']
        comprobante = request.FILES['comprobante']
        carrito = request.POST['carrito']  # Asegúrate de que este es el ID del carrito
        estado = request.POST['estado']  # Asegúrate de que este es el ID del estado

        pedido = Pedido(
            dni=dni,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            direccion=direccion,
            telefono=telefono,
            email=email,
            carrito_id=carrito,
            estado_id=estado
        )
        pedido.save()
        pedido.comprobante.save(comprobante.name, comprobante)
        request.session.create()
        return redirect('/')
    return render(request, '/crear_pedido')