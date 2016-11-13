from django import forms
from apps.producto.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'marks',
        ]
        labels = {
            'name':'Nombre',
            'price':'Precio',
            'marks':'Marca',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite Producto'}),
            'price': forms.TextInput(attrs={'class':'form-control','placeholder':'Digite Precio'}),
            'marks': forms.Select(attrs={'class':'form-control'}),
        }
