from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from apps.producto.models import Product
from apps.producto.forms import ProductForm

from django.views.generic import ListView,CreateView,UpdateView,DeleteView
# Create your views here.

class ProductoList(ListView):
    model=Product
    template_name='product/product_list.html'
    #paginate_by= 2 Esto se usa cuando se quiere paginar el ejemplo se lo ve el el proyecto refugio

class ProductoCreate(CreateView):
    model= Product
    form_class= ProductForm
    template_name='product/product_form.html'
    success_url = reverse_lazy('producto:producto_listar')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return HttpResponseRedirect(self.get_success_url())

class ProductoEdit(UpdateView):
    model=Product
    form_class=ProductForm
    template_name='product/product_form.html'
    success_url=reverse_lazy('producto:producto_listar')

class ProductoDelete(DeleteView):
    model=Product
    template_name='product/product_delete.html'
    success_url=reverse_lazy('producto:producto_listar')
