# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Core.models import *
#from form import *

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import get_object_or_404

class PerfilDetail(DetailView):
	model = User
	template_name = "Perfil_Management/perfil_detail.html"

class PerfilEdit(DetailView):
	model = User
	template_name = "Perfil_Management/perfil_edit.html"

def getValor(conductor):
	vals = conductor.first().valoraciones.all()
	suma = 0.0
	for val in vals:
		suma += val.puntaje
	return "{0:.2f}".format(suma/len(vals))

def Valorar(request, pk, tipo, reserva_id, usuario_id):
	viaje = Viaje.objects.get(id=pk)
	reservas = Reserva.objects.filter(viaje=pk).filter(estado=2)
	if tipo == "Fin":
		for r in reservas:
			r.estado = 1
			r.save()
		viaje.estado = 1
		viaje.save()
		return render(request, 'Perfil_Management/completado2.html', {'tipo': tipo})

	if len(reservas) == 0:
		viaje.estado = 1
		viaje.save()
		return render(request, 'Perfil_Management/completado2.html', {'tipo': tipo})

	if (tipo == 'Conductor'):
		#trayectos = Trayecto.objects.filter(viaje=pk).filter(estado=2)
		return render(request, 'Perfil_Management/seleccionar.html', {'viaje':viaje, 'reservas':reservas, 'tipo':'Fin'})
	elif (tipo == 'Pasajero'):
		reserva = Reserva.objects.get(id = reserva_id)
		conductor = viaje.user
		aux = str(getValor(conductor))
		print(aux)
		#conductor = viaje.conductor
		return render(request, 'Perfil_Management/valorar_conductor.html', {'viaje': viaje, 'reserva': reserva, 'conductor': conductor, 'valor': aux})

def ValorarPasajero(request, viaje_id, reserva_id):	
	viaje = Viaje.objects.get(id=viaje_id)
	usuario = viaje.user.first()

	val = Valoracion()
	estrella = request.POST.get("estrellas")
	
	if estrella == "5": val.puntaje = 5
	elif estrella == "4": val.puntaje = 4
	elif estrella == "3": val.puntaje = 3
	elif estrella == "2": val.puntaje = 2
	elif estrella == "1": val.puntaje = 1

	comentario = request.POST.get("Comentario")
	val.comentario = comentario

	val.save()
	usuario.valoraciones.add(val)
	usuario.save()

	reserva = Reserva.objects.get(id=reserva_id)
	reserva.estado = 1
	reserva.save()
	return Valorar(request, viaje_id, 'Pasajero', reserva_id, usuario.id)

def ValorarConductor(request, viaje_id, reserva_id):
	
	viaje = Viaje.objects.get(id=viaje_id)
	reserva = Reserva.objects.get(id = reserva_id)
	usuario = reserva.user.first()

	if request.method == "POST" and reserva.estado != 2:

		val = Valoracion()
		estrella = request.POST.get("estrellas")
		
		if estrella == "5": val.puntaje = 5
		elif estrella == "4": val.puntaje = 4
		elif estrella == "3": val.puntaje = 3
		elif estrella == "2": val.puntaje = 2
		elif estrella == "1": val.puntaje = 1

		comentario = request.POST.get("Comentario")
		val.comentario = comentario

		val.save()
		usuario.valoraciones.add(val)
		usuario.save()

		reserva = Reserva.objects.get(id=reserva_id)
		reserva.estado = 1
		reserva.save()
		return Valorar(request, viaje_id, 'Conductor', reserva_id, usuario.id)
	else:
		reserva.estado = 3
		reserva.save()
		aux = str(getValor(reserva.user))
		print(aux)
		#conductor = viaje.conductor
		return render(request, 'Perfil_Management/valorar_pasajero.html', {'viaje': viaje, 'reserva': reserva, 'pasajero': reserva.user, 'valor': aux})
