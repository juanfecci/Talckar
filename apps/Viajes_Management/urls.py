from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [
    url(r'^viaje$', ViajeList.as_view(), name='Viaje_List'),
    url(r'^viajeCreate$', ViajeCreate, name='Viaje_Create')
]

