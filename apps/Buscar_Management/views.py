# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from Core.models import *
from form import *

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import get_object_or_404

class BuscarList(ListView):
	model = Viaje
	template_name = "Buscar_Management/viaje_list.html"
	def get_queryset(self):
		cordx1 = float(self.request.GET.get('cordx1'))
		cordy1 = float(self.request.GET.get('cordy1'))
		cordx2 = float(self.request.GET.get('cordx2'))
		cordy2 = float(self.request.GET.get('cordy2'))
		fecha = self.request.GET.get('fecha')
		#d = self.request.GET.get('d')
		viajes = Viaje.objects.all()
		excl = []
		for v in viajes:
			if not (v.verificar(cordx1, cordy1, cordx2, cordy2, fecha) != (-1, -1)):
				excl.append(v)

		for v in excl:
			viajes = viajes.exclude(pk=v.pk)
		return viajes


def Buscar(request):
	if request.method == "POST":
		viajes = Viaje.objects.all()
		b = False

		cordx1 = float(request.POST.get('lati1'))
		cordy1 = float(request.POST.get('long1'))

		cordx2 = float(request.POST.get('lati2'))
		cordy2 = float(request.POST.get('long2'))

		fecha = request.POST.get('fecha_inicio')

		for v in viajes:
			
			if v.verificar(cordx1, cordy1, cordx2, cordy2, fecha) != (-1, -1):
				b = True
				break

		if b:
			return redirect("show?cordx1="+str(cordx1)+"&cordy1="+str(cordy1)+"&cordx2="+str(cordx2)+"&cordy2="+str(cordy2) +"&fecha="+str(fecha))

		else:
			return render(request, 'Buscar_Management/buscar_error.html', {} )

	return render(request, 'Buscar_Management/buscar.html', {})


class BuscarDetail(DetailView):
	model = Viaje
	template_name = "Buscar_Management/buscar_detail.html"

def Error(request):
	if request.method =="Error":
		form = BuscarForm(request.POST)
		return render(request, 'Buscar_Management/buscar.html', {'form': form} )

def CrearReserva(request, id, cordx1, cordx2, cordy1, cordy2):
	if request.method == "POST":
		usuario = request.user
		viaje = Viaje.objects.get(id=id)
		res = viaje.verificar(float(cordx1), float(cordy1), float(cordx2), float(cordy2), "")
		par1 = res[0]
		par2 = res[1]

		tramo = Tramo.objects.filter(viaje=id).filter(origen=par1).filter(destino=par2)
		if len(tramo) == 0:
			tramo = Tramo()
			tramo.save()
			tramo.km = 1000 # Ver sistema de de kilometros
			tramo.precio = 1000 # Y de precio
			tramo.origen = par1
			tramo.destino = par2
			tramo.viaje = viaje
			tramo.save()

		else:
			tramo = tramo.first()

		try:
			print(1)
			verificador = False
			#Posible sistema usando un for, plazas del vehiculo establecido en el viaje, hacer lista con nombres y iterarar con eso para los get 

			if request.POST.get("plaza1"):
				print(2.5)
				reserva = Reserva()
				print(2.8)
				reserva.posicion = 1
				reserva.estado = -3
				reserva.tramo = tramo
				reserva.viaje = viaje
				reserva.save()
				print(2.9)
				usuario.reservas.add(reserva)
				print(2.91)
				verificador = True

			print(2)
			if request.POST.get("plaza2"):
				reserva = Reserva()
				reserva.posicion = 2
				reserva.estado = -3
				reserva.tramo = tramo
				reserva.viaje = viaje
				reserva.save()
				usuario.reservas.add(reserva)
				verificador = True

			print(3)
			if request.POST.get("plaza3"):
				print(1)
				reserva = Reserva()
				reserva.posicion = 3
				reserva.estado = -3
				reserva.tramo = tramo
				print(2)
				reserva.viaje = viaje
				print(3)
				reserva.save()
				print(4)
				usuario.reservas.add(reserva)
				print(5)
				verificador = True

			print(4)
			if request.POST.get("plaza4"):
				reserva = Reserva()
				reserva.posicion = 4
				reserva.estado = -3
				reserva.tramo = tramo
				reserva.viaje = viaje
				reserva.save()
				usuario.reservas.add(reserva)
				verificador = True
			print(4)
			return render(request, 'Buscar_Management/correcto.html')

		except:
			print("Error!!!!!!!!!!!!!")
		'''

		trayecto = Trayecto()
		trayecto.save()

		try:
			trayecto.precio = viaje.precio
			trayecto.origen = par1
			trayecto.destino = par2
			trayecto.estado = -1
			trayecto.viaje = viaje

			if request.POST.get("plaza1"):
				plaza1 = Plaza()
				plaza1.save()
				plaza1.posicion = 1

			if request.POST.get("plaza2"):
				plaza2 = Plaza()
				plaza2.save()
				plaza2.posicion = 2

			if request.POST.get("plaza3"):
				plaza3 = Plaza()
				plaza3.save()
				plaza3.posicion = 3

			if request.POST.get("plaza4"):
				plaza4 = Plaza()
				plaza4.save()
				plaza4.posicion = 4

			trayecto.save()
			usuario.trayectos.add(trayecto)
			return render(request, 'Buscar_Management/correcto.html')

		except:
			print("Error!!!!!!!!!!!!!")
			trayecto.delete()
		'''
	print("Realmente no hubo Post")
	return render(request, 'Buscar_Management/correcto.html')

	