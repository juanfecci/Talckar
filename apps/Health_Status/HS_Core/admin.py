# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

#HEALTH STATUS

class SiteAdmin(admin.ModelAdmin):
	list_display = ('name','url','interval')

class HeartBeatAdmin(admin.ModelAdmin):
	list_display = ('site','status','date','responseTime')

admin.site.register(Site, SiteAdmin)
admin.site.register(HeartBeat, HeartBeatAdmin)
