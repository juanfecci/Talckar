from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [

    url(r'^perfil/(?P<pk>\d+)$', PerfilDetail, name='Perfil_Detail'),
    url(r'^MasValoraciones/(?P<pk>\d+)$', MasValoraciones, name='MasValoraciones'),
    url(r'^perfil/edit/(?P<pk>\d+)$', PerfilEdit.as_view(), name='Perfil_Edit'),
    url(r'^EditarPerfil/$', EditarPerfil, name='EditarPerfil'),
    url(r'^EditarFoto/$', EditarFoto, name='EditarFoto'),
    url(r'^EditarVehiculo/$', EditarVehiculo, name='EditarVehiculo'),
    url(r'^EditarFotoVehiculo/$', EditarFotoVehiculo, name='EditarFotoVehiculo'),
    url(r'^VerPerfil/(?P<pk>\d+)$', VerPerfil, name='VerPerfil'),
    url(r'^DetalleVehiculo/(?P<pk>\d+)$', DetalleVehiculo, name='DetalleVehiculo'),
    url(r'^Valorar/(?P<pk>\d+)/(?P<tipo>\w+)/(?P<reserva_id>\d+)/(?P<usuario_id>\d+)/$', Valorar, name='Valorar'),
    url(r'^Administrar/Pasa/(?P<viaje_id>\d+)/(?P<reserva_id>\d+)/$', ValorarPasajero, name='Valorar_Pasajero'),
    url(r'^Administrar/Pasa2/(?P<viaje_id>\d+)/(?P<reserva_id>\d+)/$', ValorarConductor, name='Valorar_Conductor'),
#    url(r'^buscar_error$', Buscar, name='Buscar_Create'),
#    url(r'^show/$', BuscarList.as_view() , name='show')

]