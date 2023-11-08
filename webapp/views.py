from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from producto.models import *
from cart.cart import Cart

from webapp.templatetags.cart_extras import cart_total
from django.views.decorators.clickjacking import xframe_options_exempt


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

    productos_list = Producto.objects.order_by('name')
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

    return render(request, 'catalogo.html',
                  {'productos': productos, 'categorias': categorias, 'colores': colores, 'tallas': tallas})


def detalleProducto(request, id):
    # producto = Producto.objects.get(pk=id)
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'detalleProducto.html', {'producto': producto})


def cart_add(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.add(product=product)
    return redirect("/catalogo")


def item_clear(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.remove(product)
    return redirect("/cart/cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    cart.add(product=product)
    return redirect("/cart/cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Producto.objects.get(id=id)
    if product.id in cart.cart and cart.cart[product.id]['quantity'] <= 1:
        cart.remove(product)
    else:
        cart.decrement(product=product)
    return redirect("/cart/cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/catalogo")


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@xframe_options_exempt
def payment_form(request):
    if 'cart' not in request.session or not request.session['cart']:
        return redirect('/cart_detail')
    # Aquí va tu lógica para mostrar el formulario de pago
    total_pago = cart_total()
    return render(request, 'cart/payment_form.html', {'total_pago': total_pago})
