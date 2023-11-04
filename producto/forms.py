from django.forms import ModelForm

from producto.models import *


class PoloForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class TallaForm(ModelForm):
    class Meta:
        model = Talla
        fields = '__all__'


class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = '__all__'


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
