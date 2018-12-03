# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect

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
		#form = ViajeForm(request.POST)
		#if form.is_valid():
			viaje = Viaje()
			viaje.save()
			viaje.id_viaje = 7
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
			usuario.viajes.add(viaje)
			return redirect('http://127.0.0.1:8000/Viajes_Management/viajeCreate/agregar')
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

def AgregarParadas(request):
	usuario = request.user
	if request.method == "POST":
		viaje = usuario.viajes.last()
		par2 = Parada()
		par2.id_parada = Parada.objects.count() +1
		par2.nombre = request.POST.get('parada')
		#par2.coordenada_x = request.POST.get('lati1')
		#par2.coordenada_y = request.POST.get('long1')
		par2.coordenada_x = 200
		par2.coordenada_y = 200
		par2.fecha = request.POST.get('fecha_inicio')
		par2.hora = request.POST.get('hora_inicio')
		par2.save()
		viaje.paradas.add(par2)

		return render(request,'Viajes_Management/agregar_paradas.html')
	else:
		form = ViajeForm()
		return render(request, 'Viajes_Management/agregar_paradas.html', {'form': form} )		

def Viaje2(request):
	usuario = request.user
	if request.method == "POST":
		form = ViajeForm(request.POST)
		viaje = usuario.viajes.last()
		viaje.tarifaPreferencia = form['tarifa']
		viaje.maletero = form['maletero']
		viaje.mascota = form['mascota']
		return redirect('/')
	else:
		form = ViajeForm()
		return render(request, 'Viajes_Management/Viaje2.html', {'form': form} )		