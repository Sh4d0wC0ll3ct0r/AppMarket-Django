from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from apps.producto.models import Product
from apps.producto.forms import ProductForm

from django.views.generic import ListView,CreateView
# Create your views here.

class ProductoList(ListView):
    model=Product
    template_name='product/product_list.html'
    #paginate_by= 2 Esto se usa cuando se quiere paginar el ejemplo se lo ve el el proyecto refugio

class ProductoCreate(CreateView):
    model= Product
    form_class= ProductForm
    template_name='product/product_create.html'
    success_url = reverse_lazy('producto:producto_listar')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return HttpResponseRedirect(self.get_success_url())
