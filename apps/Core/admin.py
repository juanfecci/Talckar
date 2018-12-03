# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

from .models import *


class ClientAdmin(admin.ModelAdmin):
	list_display = ('name',)
    

class ModuleAdmin(admin.ModelAdmin):
	pass

class UserAdmin(BaseUserAdmin):
	fieldsets = BaseUserAdmin.fieldsets
	fieldsets += (
	('Minerva', {'fields':['clients','activeClient', 'datos_conductor', 'correo', 'profesion', 'interes', 'fumador', 'foto', 'viajes', 'trayectos']}),
	)

class ConductorAdmin(admin.ModelAdmin):
	list_display = ('licencia', 'fecha_obtencion')

class ViajeAdmin(admin.ModelAdmin):
	list_display = ('tarifaPreferencias', )

class ParadaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'coordenada_x', 'coordenada_y')

class TrayectoAdmin(admin.ModelAdmin):
	list_display = ('precio',)

class PlazaAdmin(admin.ModelAdmin):
	list_display = ('posicion',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Viaje, ViajeAdmin)
admin.site.register(Parada, ParadaAdmin)
admin.site.register(Trayecto, TrayectoAdmin)
admin.site.register(Plaza, PlazaAdmin)