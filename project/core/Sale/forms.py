from django import forms
from ..erp.models import Category

# Formulario para crear o actualizar una categoría
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'