from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [
    url(r'^trayecto$', TrayectoList.as_view(), name='Trayecto_List'),
    url(r'^trayecto/(?P<pk>\d+)$', TrayectoDetail.as_view(), name='Trayecto_Detail')
]

