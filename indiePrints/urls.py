"""
URL configuration for indiePrints project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from producto import views as vproducto
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('administrar', views.administrar, name='administrar'),
    path('salir/', views.salir, name='salir'),
    path('detalleProducto/<int:id>', views.detalleProducto, name='detalleProducto'),

    # CRUD POLOS
    path('verpolos/', vproducto.ver_polos, name='verpolos'),
    path('agregarpolo/', vproducto.agregar_polo, name='agregarpolo'),
    path('editarpolo/<int:id>', vproducto.editar_polo, name='editarpolo'),
    path('eliminarpolo/<int:id>', vproducto.eliminar_polo, name='eliminarpolo'),

    # CRUD TALLAS
    path('vertallas/', vproducto.ver_tallas, name='vertallas'),
    path('agregartalla/', vproducto.agregar_talla, name='agregartalla'),
    path('editartalla/<int:id>', vproducto.editar_talla, name='editartalla'),
    path('eliminartalla/<int:id>', vproducto.eliminar_talla, name='eliminartalla'),

    # CRUD CATEGORIAS
    path('vercategorias/', vproducto.ver_categorias, name='vercategorias'),
    path('agregarcategoria/', vproducto.agregar_categoria, name='agregarcategoria'),
    path('editarcategoria/<int:id>', vproducto.editar_categoria, name='editarcategoria'),
    path('eliminarcategoria/<int:id>', vproducto.eliminar_categoria, name='eliminarcategoria'),

    # CRUD COLORES
    path('vercolores/', vproducto.ver_colores, name='vercolores'),
    path('agregarcolor/', vproducto.agregar_color, name='agregarcolor'),
    path('editarcolor/<int:id>', vproducto.editar_color, name='editarcolor'),
    path('eliminarcolor/<int:id>', vproducto.eliminar_color, name='eliminarcolor'),

    # CRUD MATERIALES
    path('vermateriales/', vproducto.ver_materiales, name='vermateriales'),
    path('agregarmaterial/', vproducto.agregar_material, name='agregarmaterial'),
    path('editarmaterial/<int:id>', vproducto.editar_material, name='editarmaterial'),
    path('eliminarmaterial/<int:id>', vproducto.eliminar_material, name='eliminarmaterial'),

    # ADMINISTRAR PEDIDOS
    path('verpedidos/', vproducto.ver_pedidos, name='verpedidos'),
    path('editarpedido/<int:id>', vproducto.editar_pedidos, name='editarpedido'),

    # CARRITO
    path('producto_a_carrito/<int:producto_id>/', views.producto_a_carrito, name='producto_a_carrito'),
    path('mostrar_carrito/', views.mostrar_carrito, name='mostrar_carrito'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    path('eliminar_carrito/', views.eliminar_carrito, name='eliminar_carrito'),
    path('aumentar_cantidad/<int:producto_id>/', views.aumentar_cantidad, name='aumentar_cantidad'),
    path('disminuir_cantidad/<int:producto_id>/', views.disminuir_cantidad, name='disminuir_cantidad'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),

    # COMPRAR PEDIDO
    path('crear_pedido/', views.crear_pedido, name='crear_pedido'),
    path('detalles_carrito/<int:carrito_id>/', views.detalles_carrito, name='detalles_carrito'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Indie Prints"
admin.site.site_title = "Indie Prints | Administrador"
admin.site.index_title = "Indie prints | Administrador"
