# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect

from django.shortcuts import render

from Core.models import *
from form import *

from datetime import datetime
from datetime import timedelta

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
		return ViajeCreate4(request)

	return render(request, 'Viajes_Management/viaje_create1.html', {} )

def ViajeCreate4(request):
	usuario = request.user
	if request.method == "POST":
		viaje = Viaje()
		viaje.save()
		viaje.estado = -10

		par1 = Parada()
		par1.nombre =  request.POST.get('origen')
		par1.coordenada_x = request.POST.get('lati1')
		par1.coordenada_y = request.POST.get('long1')
		par1.fecha = request.POST.get('fecha_inicio')
		par1.hora =request.POST.get('hora_inicio')

		par2 = Parada()
		par2.nombre = request.POST.get('destino')
		par2.coordenada_x = request.POST.get('lati2')
		par2.coordenada_y = request.POST.get('long2')
		par2.fecha = request.POST.get('fecha_final')
		print(request.POST.get('fecha_final'))
		_fecha1 = datetime.strptime(par1.fecha, '%Y-%m-%d')
		_fecha2 = datetime.strptime(par2.fecha, '%Y-%m-%d')
		print(_fecha1)
		print(_fecha2)
		print(_fecha2 - _fecha1)
		print(_fecha1 - _fecha2)
		if(_fecha2 - _fecha1 > timedelta(days = 1)): #no viajes largos
			return render(request, 'Viajes_Management/viajes_create.html', {'error_flag': 1})
		elif(_fecha2 - _fecha1 < timedelta(days = 0)): #no viajes en el tiempo
			return render(request, 'Viajes_Management/viajes_create.html', {'error_flag': 2})
		print(type(request.POST.get('fecha_final')))
		#print(par2.fecha - par1.fecha)
		par2.hora = request.POST.get('hora_final')
		par2.save()
		par1.save()

		viaje.origen = par1
		viaje.destino = par2

		viaje.paradas.add(par1)
		viaje.paradas.add(par2)
		usuario.viajes.add(viaje)
		#viaje.conductor = usuario
		viaje.save()
		usuario.save()
		return AgregarParadas(request)
	else:
		form = ViajeForm()
		return render(request, 'Viajes_Management/viajes_create.html', {'form': form} )		
'''
class ViajeDetail(DetailView):
	model = Viaje
	template_name = "Viajes_Management/viaje_detail.html"
'''

def getValor(conductor):
	vals = conductor.first().valoraciones.all()
	suma = 0.0
	for val in vals:
		suma += val.puntaje
	if len(vals) == 0:
		return 0
	return "{0:.2f}".format(suma/len(vals))

def ViajeDetail(request, pk):
	viaje = Viaje.objects.get(id=pk)
	reservas = Reserva.objects.filter(viaje=pk).exclude(estado=0)
	for r in reservas:
		r.user.first().promedioVal = getValor(r.user)
		r.user.first().save()
	return render(request, 'Viajes_Management/viaje_detail.html', {'viaje':viaje, 'reservas':reservas})	

def ViajeDelete(request, viaje_id):
	Viaje.objects.filter(id=viaje_id).delete()
	return render(request, 'Viajes_Management/correcto.html')

def AceptarPlaza(request, viaje_id, reserva_id):
	reserva = Reserva.objects.get(id=reserva_id)
	reserva.estado = 3
	reserva.save()
	return ViajeDetail(request, viaje_id)

def RechazarPlaza(request, viaje_id, reserva_id):
	reserva = Reserva.objects.get(id=reserva_id)
	reserva.estado = -2
	reserva.save()
	return ViajeDetail(request, viaje_id)

def AgregarParadas(request):
	usuario = request.user
	viaje = usuario.viajes.last()

	if request.method == "POST" and viaje.estado != -10:
		
		par2 = Parada()
		par2.nombre = request.POST.get('origen')
		par2.coordenada_x = float(request.POST.get('lati1'))
		par2.coordenada_y = float(request.POST.get('long1'))
		#par2.coordenada_x = 200
		#par2.coordenada_y = 200
		par2.fecha = str(request.POST.get('fecha_inicio'))
		par2.hora = str(request.POST.get('hora_inicio'))

		print(request.POST.get('hora_inicio'))
		print("AAAAAAAAAAAAAa")

		par2.save()
		viaje.paradas.add(par2)

		viaje.save()

		return render(request,'Viajes_Management/agregar_parada.html', {})
	else:
		viaje.estado = -9
		viaje.save()
		return render(request, 'Viajes_Management/agregar_parada.html', {} )

def ObtenerPromedio():
	viajes = Viaje.objects.all()
	suma = 0
	for v in viajes: suma += v.tarifaPreferencias
	return suma / len(viajes)

def Viaje2(request):
	usuario = request.user
	viaje = usuario.viajes.last()

	if request.method == "POST" and viaje.estado != -9:
		form = ViajeForm(request.POST)
		if form.is_valid():

			prestacion = Prestacion()
			prestacion.max_plazas = form.cleaned_data['plazas']
			prestacion.maletero = form.cleaned_data['maletero']
			prestacion.mascota = form.cleaned_data['mascota']
			prestacion.silla_ninnos = form.cleaned_data['silla']

			viaje.tarifaPreferencias = form.cleaned_data['tarifa']

			prestacion.save()
			viaje.prestacion = prestacion
			viaje.estado = -1

			viaje.save()
			return render(request, 'Viajes_Management/correcto2.html')
	else:
		form = ViajeForm()
		viaje.estado = -8
		viaje.save()

		tarifa = ObtenerPromedio()

		return render(request, 'Viajes_Management/Viaje2.html', {'form': form, 'tarifa': tarifa} )		

def VerPerfil1(request, pk):
	user = User.objects.get(id = pk)
	num_vals = len(user.valoraciones.all())
	if (num_vals >= 3):
		valoraciones = user.valoraciones.all().order_by('-id')[:3]
	else:
		valoraciones = user.valoraciones.all().order_by('-id')[:num_vals]
	return render(request, "Perfil_Management/perfil_detail22.html", {'usuario': user, 'flag': True, 'valoraciones': valoraciones, 'n': num_vals})
