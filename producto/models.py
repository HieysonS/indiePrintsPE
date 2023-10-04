from django.db import models


# Create your models here.


class Talla(models.Model):
    nombreTalla = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.nombreTalla}'


class Material(models.Model):
    nombreMaterial = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.nombreMaterial}'


class Color(models.Model):
    nombreColor = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.nombreColor}'


class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.nombreCategoria}'


class Producto(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imagenes/", verbose_name='Imagen', null=True)
    descripcion = models.CharField(max_length=255, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stock = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f'{self.nombre}' \
               f'\n - Precio: {self.precio}' \
               f' - Stock: {self.stock}'

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
