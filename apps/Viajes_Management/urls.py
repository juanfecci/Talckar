from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [
    url(r'^viaje$', ViajeList.as_view(), name='Viaje_List'),
    url(r'^viaje/(?P<pk>\d+)/$', ViajeDetail, name='Viaje_Detail'),
    url(r'^viaje/(?P<viaje_id>\d+)/(?P<reserva_id>\d+)/$', AceptarPlaza, name='Aceptar'),
    url(r'^viaje/rechazar/(?P<viaje_id>\d+)/(?P<reserva_id>\d+)/$', RechazarPlaza, name='Rechazar'),
    url(r'^viajeCreate$', ViajeCreate, name='Viaje_Create'),
    url(r'^viajeCreate/agregar$',AgregarParadas, name='Agregar_Paradas'),
    url(r'^viaje/delete/(?P<viaje_id>\d+)/$', ViajeDelete, name='Viaje_Delete'),
    url(r'^viaje/opciones$', Viaje2, name='Viaje2')
]

