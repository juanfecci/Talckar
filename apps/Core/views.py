# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from django.contrib.auth.decorators import login_required

import Core.worker_master 

from django import forms

from Core.models import *

import json

@login_required()
def home(request):
	#try: Core.worker_master.vigilant.apply_async()
	#except: print "The vigilant don't start"
	usuario = request.user
	viaje = usuario.viajes.filter(estado=2)
	if (usuario.activeClient.name == 'Conductor'):
		if len(viaje) == 0:
			viaje = usuario.viajes.filter(estado=3)
			if len(viaje) == 0:
				return render(request,'base.html',{'viajes': usuario.viajes})	
			else:
				viaje = viaje.first()
				reserva = usuario.reservas.all()
				if (len(reserva) == 0):
					return render(request, 'base.html', {})
				reserva = reserva.first()
				return render(request,'base3.html',{'viaje':viaje, 'viaje_id': viaje.id, 'tipo': usuario.activeClient.name, 'reserva_id': reserva.id, 'reserva': reserva, 'usuario_id': 1})
		else:
			viaje = viaje.first()
			return render(request,'base2.html',{'viaje':viaje})	#admin/Core/viaje/
	elif (usuario.activeClient.name == 'Pasajero'):
		reservas = usuario.reservas.filter(estado = 2)
		if (len(reservas) == 0):
			return render(request, 'base.html', {})
		reserva = reservas.first()
		viaje = reserva.viaje
		if (not viaje):
			return render(request, 'base.html', {'viajes': viaje})
		return render(request, 'base3.html', {'viaje': viaje, 'viaje_id': viaje.id, 'tipo': usuario.activeClient.name, 'reserva_id': reserva.id, 'usuario_id': usuario.id})
	else:
		return render(request, 'base.html', {'tipo': usuario.activeClient.name, 'str': "mal :("})

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

def Registrar(request):
	print("Hola")
	print(request.method)
	if request.method == "POST":
		print("AAAAAAAAAAAA")

		user = User.objects.create_user(request.POST.get('Username'), request.POST.get('Email'), request.POST.get('Password'))
		
		aux = Client.objects.get(name="Pasajero")
		user.clients.add(aux) 
		user.activeClient = aux

		form2 = ImageUploadForm(request.POST, request.FILES)

		if form2.is_valid():
			print("Wena wena")
			user.foto = form2.cleaned_data['image']

		user.save()

		print(request.POST.get('Username'))
		print(request.POST.get('Password'))
		print(request.POST.get('Celular'))

	return render(request, 'register.html', {})

def AdministrarViaje(request, pk):
	viaje = Viaje.objects.get(id=pk)
	reservas = Reserva.objects.filter(viaje=pk).filter(estado=1)

	if len(reservas) == 0:
		viaje.estado = 3
		viaje.save()
		return render(request, 'completado.html', {})

	primero = reservas.first()
	primero.estado = 2
	primero.save()
	reservas = reservas.exclude(id=primero.id)

	return render(request, 'administrar.html', {'viaje':viaje, 'reservas':reservas, 'primero':primero})

def TomarPasajero(request, viaje_id, reserva_id):
	reserva = Reserva.objects.get(id=reserva_id)
	reserva.estado = 2
	reserva.save()
	return AdministrarViaje(request, viaje_id)

# Requerido para login
@login_required()
def changeActiveClient(request,clientId):
	id_client = clientId

	user = request.user

	if user.clients.filter(id=id_client) > 0:
		user.activeClient = user.clients.filter(id=id_client)[0]
		user.save()
	return redirect(home)
