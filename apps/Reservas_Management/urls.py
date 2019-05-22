from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [
    url(r'^reserva$', ReservaList.as_view(), name='Reserva_List'),
    url(r'^reserva/(?P<pk>\d+)$', ReservaDetail.as_view(), name='Reserva_Detail'),
    url(r'^reserva/delete/(?P<tray_id>\d+)$', ReservaDelete, name='Reserva_Delete')
]

