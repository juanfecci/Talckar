from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [

    url(r'^perfil/(?P<pk>\d+)$', PerfilDetail.as_view(), name='Perfil_Detail'),
    url(r'^perfil/edit/(?P<pk>\d+)$', PerfilEdit.as_view(), name='Perfil_Edit'),
    url(r'^Valorar/(?P<pk>\d+)/$', Valorar, name='Valorar'),
    url(r'^Administrar/Pasa/(?P<viaje_id>\d+)/(?P<reserva_id>\d+)/$', ValorarPasajero, name='Valorar_Pasajero'),
#    url(r'^buscar_error$', Buscar, name='Buscar_Create'),
#    url(r'^show/$', BuscarList.as_view() , name='show')

]