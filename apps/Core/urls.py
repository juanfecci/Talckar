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
    url(r'^login', auth_views.login, {'template_name': './login.html'}, name="login"),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^$', core_views.home),
    url(r'^Task_Management/updateTask/(?P<id>.+)/(?P<status>.+)/(?P<percent>.+)/$', core_views.updateTask),
    url(r'^Task_Management/List$', core_views.taskList),
    url(r'^changeActiveClient/([0-9]+)/$', core_views.changeActiveClient, name="changeActiveClient" ),
    url(r'^Health_Status/', include('Health_Status.HS_Core.urls')),
    url(r'^WorkOrders_Management/', include('WorkOrders_Management.WM_Core.urls')),
    url(r'^Visibility_Management/', include('Visibility_Management.VIM_Core.urls')),
    url(r'^Asset_Management/', include('Asset_Management.ASE_Core.urls')),
    url(r'^Viajes_Management/', include('Viajes_Management.urls')),
    url(r'^Perfil_Management/', include('Perfil_Management.urls')),
    url(r'^Buscar_Management/', include('Buscar_Management.urls')),
    url(r'^Demo/', include('Demo.urls'))
]

#http://127.0.0.1:8000/Task_Management/updateTask/a452df87-39f1-4e3e-a926-0e3c047b5a7d/SUCCESS/-1/