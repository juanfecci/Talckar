from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^asset$', AssetList.as_view(), name='ASE_Asset_List'),
    url(r'^scans/(?P<pk>\d+)$', AssetDetail.as_view(), name='ASE_Asset_Detail'),
    url(r'^asset/create$', AssetCreate, name='ASE_Asset_Create'),
]

