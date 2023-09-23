from django.contrib import admin

from producto.models import Producto, Talla, Categoria, Color, Material

# Register your models here.
admin.site.register(Talla)
admin.site.register(Categoria)
admin.site.register(Color)
admin.site.register(Material)
admin.site.register(Producto)