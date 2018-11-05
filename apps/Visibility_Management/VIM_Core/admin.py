# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.


class ScanAdmin(admin.ModelAdmin):
	list_display = ('name', 'startDate', 'finishDate', 'task')
	
admin.site.register(Scan,ScanAdmin)


class FindingAdmin(admin.ModelAdmin):
	list_display = ('asset','scan', 'title', 'port')

admin.site.register(Finding,FindingAdmin)