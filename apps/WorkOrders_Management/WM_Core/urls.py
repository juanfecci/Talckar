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
from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [
    url(r'^dashboard$', dashboard,name="WM_Dashboard"),
    
    url(r'^inbox$', inbox,name="WM_Inbox"),


    url(r'^ticket_detail/(?P<pk>\d+)$', TicketDetail.as_view(), name='ticket_detail'),

    url(r'^following$', FollowingList.as_view(), name='WM_Following'),
    url(r'^following$', FollowingList.as_view(), name='following_list'),
    url(r'^following_detail/(?P<pk>\d+)$', FollowingDetail.as_view(), name='following_detail'),
  	url(r'^following_new$', FollowingCreate.as_view(), name='following_new'),
  	url(r'^following_edit/(?P<pk>\d+)$', FollowingUpdate.as_view(), name='following_edit'),
  	url(r'^following_delete/(?P<pk>\d+)$', FollowingDelete.as_view(), name='following_delete'),

    url(r'^comentary_new/(?P<ticketPK>\d+)$', ComentaryCreate.as_view(), name='comentary_new'),

    url(r'^escalation_new/(?P<ticketPK>\d+)$', EscalationCreate.as_view(), name='escalation_new'),


]
