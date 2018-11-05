# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Core.models import *
from form import *

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import get_object_or_404

class ViajeList(ListView):
	model = Viaje
	template_name = "Viajes_Management/viaje_list.html"
	def get_queryset(self):
		print(self.request.user)
		return self.request.user.viajes.all()

def ViajeCreate(request):
	usuario = request.user
	if request.method == "POST":
		form = ViajeForm(request.POST)
		if form.is_valid():
			viaje = Viaje()
			viaje.save()
			viaje.id_viaje = 5
			viaje.tarifaPreferencia = form.cleaned_data['tarifa']
			viaje.maletero = form.cleaned_data['maletero']
			viaje.mascota = form.cleaned_data['mascota']
			viaje.fecha = form.cleaned_data['fecha_inicio'].split()[0]
			viaje.hora = form.cleaned_data['fecha_inicio'].split()[1]

			par1 = Parada()
			par1.id_parada = 6
			par1.nombre = form.cleaned_data['origen']
			par1.coordenada_x = 200
			par1.coordenada_y = 200
			par1.fecha = form.cleaned_data['fecha_inicio'].split()[0]
			par1.hora = form.cleaned_data['fecha_inicio'].split()[1]
			par1.save()

			par2 = Parada()
			par2.id_parada = 6
			par2.nombre = form.cleaned_data['destino']
			par2.coordenada_x = 200
			par2.coordenada_y = 200
			par2.fecha = form.cleaned_data['fecha_final'].split()[0]
			par2.hora = form.cleaned_data['fecha_final'].split()[1]
			par2.save()

			viaje.origen = par1
			viaje.destino = par2

			viaje.paradas.add(par1)
			viaje.paradas.add(par2)

			p = form.cleaned_data['paradas'].split("\n")

			for i in p:
				i_2 = i.split()
				auxP = Parada()
				auxP.id_parada = 7
				auxP.nombre = i_2[0]
				auxP.coordenada_x = 200
				auxP.coordenada_y = 200
				auxP.fecha = i_2[1]
				auxP.hora = i_2[2]

				auxP.save()

				viaje.paradas.add(auxP)

			viaje.save()
			usuario.viajes.add(viaje)

			return render(request, 'Viajes_Management/viajes_create.html', {'form': form} )		

	else:
		form = ViajeForm()
	return render(request, 'Viajes_Management/viajes_create.html', {'form': form} )		
