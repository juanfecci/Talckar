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
	('Minerva', {'fields':['clients','activeClient', 'datos_conductor', 'correo', 'profesion', 'interes', 'fumador', 'foto', 'viajes', 'reservas', 'valoraciones']}),
	)

class ConductorAdmin(admin.ModelAdmin):
	list_display = ('licencia', 'fecha_obtencion')

class VehiculoAdmin(admin.ModelAdmin):
	list_display = ('marca', 'modelo', 'color', 'anno')

class ViajeAdmin(admin.ModelAdmin):
	list_display = ('tarifaPreferencias', 'estado', 'origen', 'destino')

class PrestacionAdmin(admin.ModelAdmin):
	list_display = ('maletero', 'mascota', 'silla_ninnos')

class ParadaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'coordenada_x', 'coordenada_y')

class TramoAdmin(admin.ModelAdmin):
	list_display = ('precio', 'km')

class ReservaAdmin(admin.ModelAdmin):
	list_display = ('posicion', 'estado', 'tramo', 'viaje')

class ValoracionAdmin(admin.ModelAdmin):
	list_display = ('comentario',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Viaje, ViajeAdmin)
admin.site.register(Prestacion, PrestacionAdmin)
admin.site.register(Parada, ParadaAdmin)
admin.site.register(Tramo, TramoAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Valoracion, ValoracionAdmin)