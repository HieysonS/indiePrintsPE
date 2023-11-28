from producto.models import Carrito


def carrito_cantidad(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        try:
            carrito = Carrito.objects.get(id=carrito_id)
        except Carrito.DoesNotExist:
            carrito = Carrito.objects.create()
            request.session['carrito_id'] = carrito.id
        cantidad_total = sum(item.cantidad for item in carrito.carritoproducto_set.all())
    else:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id
        cantidad_total = 0
    return {'cantidad_total': cantidad_total}