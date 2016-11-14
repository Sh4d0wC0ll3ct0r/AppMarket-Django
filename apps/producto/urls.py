from django.conf.urls import url
from apps.producto.views import ProductoList,ProductoCreate,ProductoEdit,ProductoDelete

urlpatterns = [
    #url(r'^$', MascotaList,name='index'),
    # url(r'^nuevo$', mascota_view, name='mascota_crear'), #Vista basada en Funciones
    #url(r'^nuevo$', MascotaCreate.as_view(), name='mascota_crear'), #Vista basada en Clases
    url(r'^delete/(?P<pk>\d+)$', ProductoDelete.as_view(), name='producto_eliminar'),
    url(r'^edit/(?P<pk>\d+)$', ProductoEdit.as_view(), name='producto_editar'),
    url(r'^create', ProductoCreate.as_view(), name='producto_agregar'),
    url(r'^', ProductoList.as_view(), name='producto_listar'), #Vista Basada en Funciones
]
