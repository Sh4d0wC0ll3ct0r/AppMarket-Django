from django.conf.urls import url
from apps.producto.views import MascotaList

urlpatterns = [
    #url(r'^$', MascotaList,name='index'),
    # url(r'^nuevo$', mascota_view, name='mascota_crear'), #Vista basada en Funciones
    #url(r'^nuevo$', MascotaCreate.as_view(), name='mascota_crear'), #Vista basada en Clases
    url(r'^', MascotaList.as_view(), name='mascota_listar'), #Vista Basada en Funciones

]
