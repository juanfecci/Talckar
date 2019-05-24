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

def Valorar(request, pk):
	viaje = Viaje.objects.get(id=pk)
	reservas = Reserva.objects.filter(viaje=pk).filter(estado=2)
	#trayectos = Trayecto.objects.filter(viaje=pk).filter(estado=2)

	if len(reservas) == 0:
		viaje.estado = 1
		viaje.save()
		return render(request, 'Perfil_Management/completado2.html', {})

	primero = reservas.first()

	return render(request, 'Perfil_Management/valorar.html', {'viaje':viaje, 'primero':primero})

def ValorarPasajero(request, viaje_id, reserva_id):	
	reserva = Reserva.objects.get(id=reserva_id)
	reserva.estado = 1
	reserva.save()
	return Valorar(request, viaje_id)
