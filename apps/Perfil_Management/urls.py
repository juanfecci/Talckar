from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [

    url(r'^perfil/(?P<pk>\d+)$', PerfilDetail.as_view(), name='Perfil_Detail'),
    url(r'^perfil/edit/(?P<pk>\d+)$', PerfilEdit.as_view(), name='Perfil_Edit')
#    url(r'^buscar_error$', Buscar, name='Buscar_Create'),
#    url(r'^show/$', BuscarList.as_view() , name='show')

]