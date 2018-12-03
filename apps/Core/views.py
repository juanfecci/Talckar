# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from django.contrib.auth.decorators import login_required

import Core.worker_master 

from Core.models import *

import json

@login_required()
def home(request):
	#try: Core.worker_master.vigilant.apply_async()
	#except: print "The vigilant don't start"
	usuario = request.user
	viaje = usuario.viajes.filter(estado=2)

	if len(viaje) == 0:
		viaje = usuario.viajes.filter(estado=3)
		if len(viaje) == 0:
			return render(request,'base.html',{})	
		else:
			viaje = viaje.first()
			return render(request,'base3.html',{'viaje':viaje})	

	else:
		viaje = viaje.first()
		return render(request,'base2.html',{'viaje':viaje})	

def Valorar(request, pk):
	viaje = Viaje.objects.get(id=pk)
	trayectos = Trayecto.objects.filter(viaje=pk).filter(estado=2)

	if len(trayectos) == 0:
		viaje.estado = 1
		viaje.save()
		return render(request, 'completado2.html', {})

	primero = trayectos.first()

	return render(request, 'valorar.html', {'viaje':viaje, 'primero':primero})

def ValorarPasajero(request, viaje_id, trayecto_id):	
	trayecto = Trayecto.objects.get(id=trayecto_id)
	trayecto.estado = 1
	trayecto.save()
	return Valorar(request, viaje_id)

def AdministrarViaje(request, pk):
	viaje = Viaje.objects.get(id=pk)
	trayectos = Trayecto.objects.filter(viaje=pk).filter(estado=1)

	if len(trayectos) == 0:
		viaje.estado = 3
		viaje.save()
		return render(request, 'completado.html', {})

	primero = trayectos.first()
	trayectos = trayectos.exclude(id=primero.id)

	return render(request, 'administrar.html', {'viaje':viaje, 'trayectos':trayectos, 'primero':primero})

def TomarPasajero(request, viaje_id, trayecto_id):
	trayecto = Trayecto.objects.get(id=trayecto_id)
	trayecto.estado = 2
	trayecto.save()
	return AdministrarViaje(request, viaje_id)

@login_required()
def changeActiveClient(request,clientId):
	id_client = clientId

	user = request.user

	if user.clients.filter(id=id_client) > 0:
		user.activeClient = user.clients.filter(id=id_client)[0]
		user.save()
	return redirect(home)
