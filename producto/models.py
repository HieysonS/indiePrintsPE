from django.db import models


# Create your models here.


class Talla(models.Model):
    nombreTalla = models.CharField(max_length=100, null=False, verbose_name="Talla")

    def __str__(self):
        return f'{self.nombreTalla}'


class Material(models.Model):
    nombreMaterial = models.CharField(max_length=100, null=False, verbose_name="Material")

    def __str__(self):
        return f'{self.nombreMaterial}'


class Color(models.Model):
    nombreColor = models.CharField(max_length=100, null=False, verbose_name="Color")

    def __str__(self):
        return f'{self.nombreColor}'


class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=100, null=False, verbose_name="Categoria")

    def __str__(self):
        return f'{self.nombreCategoria}'


class Producto(models.Model):
    nombre = models.CharField(max_length=255, null=False, verbose_name="Nombre")
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE, verbose_name="Talla")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Material")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name="Color")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categória")
    imagen = models.ImageField(upload_to="imagenes/", verbose_name='Imagen', null=True)
    descripcion = models.CharField(max_length=255, null=False, verbose_name='Descripción')
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='Precio')
    stock = models.PositiveIntegerField(null=False, verbose_name="Stock")

    def __str__(self):
        return f'{self.nombre}' \
               f'\n - Precio: {self.precio}' \
               f' - Stock: {self.stock}'

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
