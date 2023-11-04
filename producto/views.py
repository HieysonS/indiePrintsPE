import os
from django.shortcuts import render, get_object_or_404, redirect
from producto.forms import *
from producto.models import *


# Create your views here.


def ver_polos(request):
    cantidad_polos = Producto.objects.count()
    polos = Producto.objects.order_by('nombre')
    # polos = get_object_or_404(Producto, pk=id)
    return render(request, 'crud/polos/verpolos.html', {'cantidad_polos': cantidad_polos, 'polos': polos})

# PoloForm = modelform_factory(Producto, exclude=[])


def agregar_polo(request):
    if request.method == 'POST':
        formaPolo = PoloForm(request.POST, request.FILES)
        if formaPolo.is_valid():
            formaPolo.save()
            return redirect('verpolos')
    else:
        formaPolo = PoloForm()
    return render(request, 'crud/polos/agregarpolo.html', {'formaPolo': formaPolo})


def editar_polo(request, id):
    polo = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        formaPolo = PoloForm(request.POST, request.FILES, instance=polo)
        if formaPolo.is_valid():
            if 'imagen' in request.FILES:
                if polo.imagen:
                    os.remove(polo.imagen.path)
            formaPolo.save()
            return redirect('verpolos')
    else:
        formaPolo = PoloForm(instance=polo)
    return render(request, 'crud/polos/editarpolo.html', {'formaPolo': formaPolo})


def eliminar_polo(request, id):
    polo = get_object_or_404(Producto, pk=id)
    if polo:
        if polo.imagen:
            os.remove(polo.imagen.path)
        polo.delete()
    return redirect('verpolos')


def ver_tallas(request):
    cantidad_tallas = Talla.objects.count()
    tallas = Talla.objects.order_by('nombreTalla')
    return render(request, 'crud/tallas/vertallas.html', {'cantidad_tallas': cantidad_tallas, 'tallas': tallas})


def agregar_talla(request):
    if request.method == 'POST':
        formaTalla = TallaForm(request.POST)
        if formaTalla.is_valid():
            formaTalla.save()
            return redirect('vertallas')
    else:
        formaTalla = TallaForm()
    return render(request, 'crud/tallas/agregartalla.html', {'formaTalla': formaTalla})


def editar_talla(request, id):
    talla = get_object_or_404(Talla, pk=id)
    if request.method == 'POST':
        formaTalla = TallaForm(request.POST, instance=talla)
        if formaTalla.is_valid():
            formaTalla.save()
            return redirect('vertallas')
    else:
        formaTalla = TallaForm(instance=talla)
    return render(request, 'crud/tallas/editartalla.html', {'formaTalla': formaTalla})


def eliminar_talla(request, id):
    talla = get_object_or_404(Talla, pk=id)
    if talla:
        talla.delete()
    return redirect('/vertallas')


def ver_categorias(request):
    cantidad_categorias = Categoria.objects.count()
    categorias = Categoria.objects.order_by('nombreCategoria')
    return render(request, 'crud/categorias/vercategorias.html', {'cantidad_categorias': cantidad_categorias, 'categorias': categorias})


def agregar_categoria(request):
    if request.method == 'POST':
        formaCategoria = CategoriaForm(request.POST)
        if formaCategoria.is_valid():
            formaCategoria.save()
            return redirect('vercategorias')
    else:
        formaCategoria = CategoriaForm()
    return render(request, 'crud/categorias/agregarcategoria.html', {'formaCategoria': formaCategoria})


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        formaCategoria = CategoriaForm(request.POST, instance=categoria)
        if formaCategoria.is_valid():
            formaCategoria.save()
            return redirect('vercategorias')
    else:
        formaCategoria = CategoriaForm(instance=categoria)
    return render(request, 'crud/categorias/editarcategoria.html', {'formaCategoria': formaCategoria})


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if categoria:
        categoria.delete()
    return redirect('/vercategorias')


def ver_colores(request):
    cantidad_colores = Color.objects.count()
    colores = Color.objects.order_by('nombreColor')
    return render(request, 'crud/colores/vercolores.html', {'cantidad_colores': cantidad_colores, 'colores': colores})


def agregar_color(request):
    if request.method == 'POST':
        formaColor = ColorForm(request.POST)
        if formaColor.is_valid():
            formaColor.save()
            return redirect('vercolores')
    else:
        formaColor = ColorForm()
    return render(request, 'crud/colores/agregarcolor.html', {'formaColor': formaColor})


def editar_color(request, id):
    color = get_object_or_404(Color, pk=id)
    if request.method == 'POST':
        formaColor = ColorForm(request.POST, instance=color)
        if formaColor.is_valid():
            formaColor.save()
            return redirect('vercolores')
    else:
        formaColor = ColorForm(instance=color)
    return render(request, 'crud/colores/editarcolor.html', {'formaColor': formaColor})


def eliminar_color(request, id):
    color = get_object_or_404(Color, pk=id)
    if color:
        color.delete()
    return redirect('/vercolores')


def ver_materiales(request):
    cantidad_materiales = Material.objects.count()
    materiales = Material.objects.order_by('nombreMaterial')
    return render(request, 'crud/materiales/vermateriales.html', {'cantidad_materiales': cantidad_materiales, 'materiales': materiales})


def agregar_material(request):
    if request.method == 'POST':
        formaMaterial = MaterialForm(request.POST)
        if formaMaterial.is_valid():
            formaMaterial.save()
            return redirect('vermateriales')
    else:
        formaMaterial = MaterialForm()
    return render(request, 'crud/materiales/agregarmaterial.html', {'formaMaterial': formaMaterial})


def editar_material(request, id):
    material = get_object_or_404(Color, pk=id)
    if request.method == 'POST':
        formaMaterial = MaterialForm(request.POST, instance=material)
        if formaMaterial.is_valid():
            formaMaterial.save()
            return redirect('vermateriales')
    else:
        formaMaterial = MaterialForm(instance=material)
    return render(request, 'crud/materiales/editarmaterial.html', {'formaMaterial': formaMaterial})


def eliminar_material(request, id):
    material = get_object_or_404(Material, pk=id)
    if material:
        material.delete()
    return redirect('/vermateriales')


