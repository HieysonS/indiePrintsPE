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
    name = models.CharField(max_length=255, null=False, verbose_name="Nombre")
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE, verbose_name="Talla")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Material")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name="Color")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categória")
    image = models.ImageField(upload_to="imagenes/", verbose_name='Imagen', null=True)
    descripcion = models.CharField(max_length=255, null=False, verbose_name='Descripción')
    price = models.FloatField(null=False, verbose_name='Precio')
    stock = models.PositiveIntegerField(null=False, verbose_name="Stock")

    def __str__(self):
        return f'{self.name}' \
               f'\n - Precio: {self.price}' \
               f' - Stock: {self.stock}'

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


class Estado(models.Model):
    nombreEstado = models.CharField(max_length=100, verbose_name='nombre')

    def __str__(self):
        return f'{self.nombreEstado}'


class Pedido(models.Model):
    dni = models.CharField(max_length=8, unique=True, verbose_name='dni')
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    apellido_paterno = models.CharField(max_length=100, verbose_name='apellido_paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='apellido_materno')
    direccion = models.CharField(max_length=200, verbose_name='direccion')
    telefono = models.CharField(max_length=15, verbose_name='telefono')
    email = models.EmailField(max_length=100, unique=True, verbose_name='email')
    compra = models.PositiveIntegerField(null=False, verbose_name="compra")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='total')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name="estado")

    def __str__(self):
        return f'{self.dni} |' \
               f' {self.nombre} {self.apellido_paterno} {self.apellido_materno} |' \
               f' {self.direccion} |' \
               f' {self.telefono} |' \
               f' {self.email} |' \
               f' {self.compra} |' \
               f' {self.total} '







