from django.shortcuts import render
from apps.producto.models import Product

from django.views.generic import ListView
# Create your views here.

class MascotaList(ListView):
    model=Product
    template_name='product/product_list.html'
    paginate_by= 2
