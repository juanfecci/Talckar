from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [
    url(r'^scans$', ScanList.as_view(), name='VIM_Scan_List'),
    url(r'^scans/finding$', FindingList.as_view(), name='VIM_Finding_List'),
    url(r'^scans/finding/(?P<pk>\d+)$', FindingDetail.as_view(), name='VIM_Finding_Detail'),
    url(r'^scans/asset$', AssetList.as_view(), name='VIM_Asset_List'),
    url(r'^scans/asset/(?P<pk>\d+)$', AssetDetail.as_view(), name='VIM_Asset_Detail'),
    url(r'^scans/new$', ScanCreate, name='VIM_Scan_New'),
    url(r'^scans/(?P<pk>\d+)$', ScanDetail, name='VIM_Scan_Detail'),
    url(r'^scans/(?P<pk>\d+)/update$', ScanUpdate.as_view(), name='VIM_Scan_Update'),
    url(r'^scans/(?P<pk>\d+)/delete$', ScanDelete.as_view(), name='VIM_Scan_Delete'),
    url(r"^scans/finish/(?P<task>.+)/(?P<url>.+)/(?P<title>.+)/(?P<port>.+)/(?P<status>.+)/(?P<image>.+)/$", ScanFinish)
]

