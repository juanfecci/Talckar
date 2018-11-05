# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# Register your models here.

class AssetAdmin(admin.ModelAdmin):
	list_display = ('address',)

admin.site.register(Asset,AssetAdmin)


class TagAdmin(admin.ModelAdmin):
	list_display = ('code', 'tag')

admin.site.register(Tag,TagAdmin)