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
		return ViajeCreate2(request, True)

	return render(request, 'Viajes_Management/viaje_create1.html', {} )

def ViajeCreate2(request, first=False):
	usuario = request.user
	if first:
		par1 = dict()
		par2 = dict()
		par1.nombre =  request.POST.get('origen')
		par1.coordenada_x = request.POST.get('lati1')
		par1.coordenada_y = request.POST.get('long1')
		par1.fecha = request.POST.get('fecha_inicio')
		par1.hora =request.POST.get('hora_inicio')

		par2.nombre = request.POST.get('destino')
		par2.coordenada_x = request.POST.get('lati2')
		par2.coordenada_y = request.POST.get('long2')
		par2.fecha = request.POST.get('fecha_final')
		par2.hora = request.POST.get('hora_final')


def ViajeCreate4(request):
	usuario = request.user
	if request.method == "POST":
		response = ''
		for key,value in request.POST.items():
			response += 'key:%s value:%s\n' % (key,value)
			print(response)

		form = ViajeForm(request.POST)
		if form.is_valid():
			viaje = Viaje()
			viaje.save()
			viaje.id_viaje = 7
			viaje.tarifaPreferencia = form.cleaned_data['tarifa']
			viaje.maletero = form.cleaned_data['maletero']
			viaje.mascota = form.cleaned_data['mascota']
			viaje.fecha = request.POST.get('fecha_inicio')
			viaje.hora = request.POST.get('hora_inicio')

			par1 = Parada()
			par1.id_parada = 10
			par1.nombre =  request.POST.get('origen')
			par1.coordenada_x = request.POST.get('lati1')
			par1.coordenada_y = request.POST.get('long1')
			par1.fecha = request.POST.get('fecha_inicio')
			par1.hora =request.POST.get('hora_inicio')
			par1.save()

			par2 = Parada()
			par2.id_parada = 8
			par2.nombre = request.POST.get('destino')
			par2.coordenada_x = request.POST.get('lati2')
			par2.coordenada_y = request.POST.get('long2')
			par2.fecha = request.POST.get('fecha_final')
			par2.hora = request.POST.get('hora_final')
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
'''
class ViajeDetail(DetailView):
	model = Viaje
	template_name = "Viajes_Management/viaje_detail.html"
'''
def ViajeDetail(request, pk):
	viaje = Viaje.objects.get(id=pk)
	trayectos = Trayecto.objects.filter(viaje=pk).exclude(estado=0)
	return render(request, 'Viajes_Management/viaje_detail.html', {'viaje':viaje, 'trayectos':trayectos})	

def ViajeDelete(request, viaje_id):
	Viaje.objects.filter(id=viaje_id).delete()
	return render(request, 'Viajes_Management/correcto.html')

def AceptarPlaza(request, viaje_id, trayecto_id):
	trayecto = Trayecto.objects.get(id=trayecto_id)
	trayecto.estado = 1
	trayecto.save()
	return ViajeDetail(request, viaje_id)

def RechazarPlaza(request, viaje_id, trayecto_id):
	trayecto = Trayecto.objects.get(id=trayecto_id)
	trayecto.estado = 0
	trayecto.save()
	return ViajeDetail(request, viaje_id)