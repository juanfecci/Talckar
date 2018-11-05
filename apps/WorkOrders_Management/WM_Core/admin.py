# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
#HEALTH STATUS

class TicketAdmin(admin.ModelAdmin):
	list_display = ('created','id_petition','id_workOrder','resume')
	search_fields = ('created','id_petition','id_workOrder','resume')

class DetailAdmin(admin.ModelAdmin):
	list_display = ('ticket','date','comment','forwarder')
	search_fields = ('ticket__id_workOrder','date','comment','forwarder')

class FollowingAdmin(admin.ModelAdmin):
	list_display = ('ticket','last_escaling','active')
	search_fields = ('ticket__id_workOrder','last_escaling','active')

class InboxAdmin(admin.ModelAdmin):
	list_display = ('ticket','date_in','date_out',"active")
	search_fields = ("active",)

class LogAdmin(admin.ModelAdmin):
	list_display = ('ticket','date','user','message')
	search_fields = ('ticket__id_workOrder','user','message')

class EscalationAdmin(admin.ModelAdmin):
	list_display = ('ticket','author','method','recipient','comment','date')
	search_fields = ('ticket__id_workOrder','user','comment', "author", "method")



admin.site.register(Ticket, TicketAdmin)

admin.site.register(Detail, DetailAdmin)

admin.site.register(Following, FollowingAdmin)

admin.site.register(Inbox, InboxAdmin)

admin.site.register(Log,LogAdmin)

admin.site.register(Escalation,EscalationAdmin)
