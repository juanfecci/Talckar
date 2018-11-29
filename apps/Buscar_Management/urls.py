from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [
    url(r'^buscar$', Buscar, name='Buscar_Create'),
    url(r'^buscar_error$', Buscar, name='Buscar_Create2'),
    url(r'^show/$', BuscarList.as_view() , name='show'),
    url(r'^buscar/(?P<pk>\d+)', BuscarDetail.as_view(), name='Buscar_Detail'),
    url(r'^buscar/correcto/(?P<id>\d+)/(?P<origen>\d+)/(?P<destino>\d+)', CrearTrayecto, name='Buscar_Final'),
]