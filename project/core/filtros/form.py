from django.forms import *

from core.erp.models import Category, Product


#Usamos este porque asi non funciona con un modelo base
class TestForm(Form):
    categorias = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class': 'from-control select2'
    }))

    productos = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'from-control select2'
    }))