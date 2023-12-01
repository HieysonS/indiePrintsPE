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


class Descuento(models.Model):
    valor = models.IntegerField()

    def save(self, *args, **kwargs):
        self.valor = min(100, max(0, self.valor))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.valor}%"


class Producto(models.Model):
    nombre = models.CharField(max_length=255, null=False, verbose_name="Nombre")
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE, verbose_name="Talla")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Material")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name="Color")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categória")
    descuento = models.ForeignKey(Descuento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Descuento")
    imagen = models.ImageField(upload_to="imagenes/", verbose_name='Imagen', null=True)
    descripcion = models.CharField(max_length=255, null=False, verbose_name='Descripción')
    precio = models.FloatField(null=False, verbose_name='Precio')
    stock = models.PositiveIntegerField(null=False, verbose_name="Stock")

    def __str__(self):
        return f'{self.nombre}' \
               f'\n - Precio: {self.precio}' \
               f' - Stock: {self.stock}'

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    def precio_con_descuento(self):
        if self.descuento:
            return self.precio * (100 - self.descuento.valor) / 100
        else:
            return self.precio


class Estado(models.Model):
    nombreEstado = models.CharField(max_length=100, verbose_name='nombreEstado')

    def __str__(self):
        return f'{self.nombreEstado}'


class Carrito(models.Model):
    productos = models.ManyToManyField(Producto, through='CarritoProducto')

    def subtotal(self):
        return sum(item.subtotal for item in self.carritoproducto_set.all())

    def __str__(self):
        return f'{self.id}' \
               f'{self.subtotal()}'


class CarritoProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.producto.precio_con_descuento() * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.carrito.id}' \
               f'{self.producto.name}' \
               f'{self.cantidad}' \
               f'{self.subtotal}'


class Pedido(models.Model):
    dni = models.CharField(max_length=8, verbose_name='dni')
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    apellido_paterno = models.CharField(max_length=100, verbose_name='apellido_paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='apellido_materno')
    direccion = models.CharField(max_length=200, verbose_name='direccion')
    telefono = models.CharField(max_length=15, verbose_name='telefono')
    email = models.EmailField(max_length=100, verbose_name='email')
    comprobante = models.ImageField(upload_to="comprobantes/", verbose_name='Comprobante', null=True)
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE, null=False, verbose_name="carrito")
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, verbose_name="estado", null=True)

    @property
    def subtotal(self):
        return self.carrito.subtotal()

    def delete(self, using=None, keep_parents=False):
        self.comprobante.storage.delete(self.comprobante.name)
        super().delete()

    def __str__(self):
        return f'{self.dni} |' \
               f' {self.nombre} {self.apellido_paterno}|' \
               f' {self.direccion} |' \
               f' {self.telefono} |' \
               f' {self.email} |' \
               f' {self.fecha}' \
               f' {self.carrito} |' \
               f' {self.subtotal}'