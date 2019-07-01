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

def Registrar(request, tipo, userId=None):
	print("Hola")
	print(request.method)

	print(tipo)

	if request.method == "POST":

		if int(tipo) == 0:
			ret = createUser(request, "Pasajero")
			print(ret)
			return render(request, 'loginNEW.html', {'error': ret})

		if int(tipo) == 1:
			ret = createUser(request, "Conductor")
			print(ret)
			if ret == "Registro realizado exitosamente":
				return render(request, 'vehiculo.html', {'user': request.POST.get('Username')})
			else:
				return render(request, 'loginNEW.html', {'error': ret})

		if int(tipo) == 2:

			if not request.POST.get('Anno').isdigit():
				ret = "Error, El año no fue ingresado de forma correcta"
				return render(request, 'vehiculo.html', {'user': request.POST.get('Username'), 'error': ret})

			if not request.POST.get('nAsientos').isdigit():
				ret = "Error, El numero de asientos no fue ingresado de forma correcta"
				return render(request, 'vehiculo.html', {'user': request.POST.get('Username'), 'error': ret})

			if not request.POST.get('pCombustible').isdigit():
				ret = "Error, El precio del combustible no fue ingresado de forma correcta (debe ser solo los números)"
				return render(request, 'vehiculo.html', {'user': request.POST.get('Username'), 'error': ret})

			veh = Vehiculo()
			cond = Conductor()
			usuario = User.objects.get(username=userId)

			veh.marca = request.POST.get('marca')
			veh.modelo = request.POST.get('Modelo')

			form2 = ImageUploadForm(request.POST, request.FILES)

			if form2.is_valid():
				veh.foto_vehiculo = form2.cleaned_data['image']

			veh.color = request.POST.get('Color')
			veh.anno = request.POST.get('Anno')
			veh.numero_asientos = request.POST.get('nAsientos')
			veh.precio_combustible = request.POST.get('pCombustible')

			veh.save()

			cond.licencia = request.POST.get('licencia')
			cond.fecha_obtencion = request.POST.get('fecha')
			cond.vehiculo = veh

			cond.save()

			usuario.datos_conductor = cond

			usuario.save()

			return render(request, 'loginNEW.html', {'error': "Registro realizado exitosamente"})


	return home(request)

def createUser(request, name):

	if User.objects.filter(username=request.POST.get('Username')).exists():
		return "Error, el usuario ya existe"

	if request.POST.get('Password') != request.POST.get('Password2'):
		return "Error, contraseñas incorrectas"

	if request.POST.get('Email') != request.POST.get('Email2'):
		return "Error, correos incorrectas"

	if not request.POST.get('Celular').isdigit():
		return "Error, contraseñas incorrectas"	

	user = User.objects.create_user(request.POST.get('Username'), request.POST.get('Email'), request.POST.get('Password'))
	
	user.first_name = request.POST.get('Nombre')
	user.last_name = request.POST.get('Apellido')
	user.profesion = request.POST.get('Profesión')
	user.celular = request.POST.get('Celular')	
	user.interes = request.POST.get('Interes')
	user.fumador = request.POST.get('optradio')

	aux = Client.objects.get(name=name)
	user.clients.add(aux) 
	user.activeClient = aux

	form2 = ImageUploadForm(request.POST, request.FILES)

	if form2.is_valid():
		user.foto = form2.cleaned_data['image']

	user.save()
	return "Registro realizado exitosamente"

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
