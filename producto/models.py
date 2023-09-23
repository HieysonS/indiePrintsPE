from django.db import models

# Create your models here.


class Talla(models.Model):
    nombreTalla = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'Talla {self.id}: {self.nombreTalla}'


class Material(models.Model):
    nombreMaterial = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'Material {self.id}: {self.nombreMaterial}'


class Color(models.Model):
    nombreColor = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'Color {self.id}: {self.nombreColor}'


class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'Categoria {self.id}: {self.nombreCategoria}'


class Producto(models.Model):
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stock = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f'Producto {self.id}:' \
               f'\n{self.talla}' \
               f'\n{self.color}' \
               f'\n{self.material}' \
               f'\n{self.precio}' \
               f'\n{self.descripcion}' \
               f'\n¡Aprovecha que solo queda {self.stock} unidades en stock...!'
