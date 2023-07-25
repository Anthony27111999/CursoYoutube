from django.forms import ModelForm, TextInput, Textarea

from core.erp.models import Category


class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                }),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Description',
                    'rows': 5,
                    'cols': 3
                }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.visible_fields():
            fields.field.widget.attrs['class'] = 'form-control'
            fields.field.widget.attrs['autocomplete'] = 'off'
            fields.field.widget.attrs['autofocus'] = True

    def clean(self):
        clearned = super().clean()
        if len(clearned['name']) > 50:
            self.add_error('name', 'Faltan caracteres')
        return clearned
