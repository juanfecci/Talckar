"""minerva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin

from Core import views as core_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login', auth_views.login, {'template_name': './loginNEW.html'}, name="login"),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^register/(?P<tipo>\d+)/$', core_views.Registrar, name="Registrar"),
    url(r'^register/(?P<tipo>\d+)/(?P<userId>[\w\-]+)/$', core_views.Registrar, name="Registrar2"),
    url(r'^$', core_views.home, name="Index_Base"),
    url(r'^Administrar/(?P<pk>\d+)/$', core_views.AdministrarViaje, name='Administrar_Viaje'),
    url(r'^Administrar/Toma/(?P<viaje_id>\d+)/(?P<reserva_id>\d+)/$', core_views.TomarPasajero, name='Tomar_Pasajero'),
    url(r'^changeActiveClient/([0-9]+)/$', core_views.changeActiveClient, name="changeActiveClient" ),

    url(r'^apiViajes$', core_views.apiViajes, name="apiViajes" ),
    url(r'^apiReservas$', core_views.apiReservas, name="apiReservas" ),
    url(r'^apiReservasCond$', core_views.apiReservasCond, name="apiReservasCond" ),

    url(r'^apiNotificarViaje/(?P<id>\d+)/$', core_views.apiNotificarViaje, name='apiNotificarViaje'),
    url(r'^apiNotificarReserva/(?P<id>\d+)/$', core_views.apiNotificarReserva, name='apiNotificarReserva'),

    url(r'^apiTest1$', core_views.apiTest1, name="apiTest1" ),
    url(r'^apiTest2$', core_views.apiTest2, name="apiTest2" ),
    url(r'^Viajes_Management/', include('Viajes_Management.urls')),
    url(r'^Perfil_Management/', include('Perfil_Management.urls')),
    url(r'^Buscar_Management/', include('Buscar_Management.urls')),
    url(r'^Reservas_Management/', include('Reservas_Management.urls'))
]

#http://127.0.0.1:8000/Task_Management/updateTask/a452df87-39f1-4e3e-a926-0e3c047b5a7d/SUCCESS/-1/