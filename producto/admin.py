from django.contrib import admin

from producto.models import *

# Register your models here.
admin.site.register(Talla)
admin.site.register(Categoria)
admin.site.register(Color)
admin.site.register(Material)
admin.site.register(Producto)
admin.site.register(Estado)
admin.site.register(Pedido)
