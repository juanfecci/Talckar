# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

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
		o = self.request.GET.get('o')
		d = self.request.GET.get('d')
		viajes = Viaje.objects.all()
		excl = []
		for v in viajes:
			if not (v.paradas.filter(nombre=o).exists() and v.paradas.filter(nombre=d).exists()):
				excl.append(v)

		for v in excl:
			viajes = viajes.exclude(pk=v.pk)
		return viajes


def Buscar(request):
	if request.method == "POST":
		form = BuscarForm(request.POST)
		viajes = Viaje.objects.all()
		b = False
		for v in viajes:
			print(form)
			print(form.cleaned_data['origen'])
			print(form.cleaned_data['destino'])
			if v.paradas.filter(nombre=form.cleaned_data['origen']).exists() and v.paradas.filter(nombre=form.cleaned_data['destino']).exists():
				b = True
				break

		if b:
			return HttpResponseRedirect("http://127.0.0.1:8000/Buscar_Management/show?o="+form.cleaned_data['origen']+"&d="+form.cleaned_data['destino'])

		else:
			form = BuscarForm()
			return render(request, 'Buscar_Management/buscar_error.html', {'form': form} )

	else:
		form = BuscarForm()

	return render(request, 'Buscar_Management/buscar.html', {'form': form} )


class BuscarDetail(DetailView):
	model = Viaje
	template_name = "Buscar_Management/buscar_detail.html"

def Error(request):
	if request.method =="Error":
		form = BuscarForm(request.POST)
		return render(request, 'Buscar_Management/buscar.html', {'form': form} )

def CrearTrayecto(request, id, origen, destino):
	if request.method == "POST":
		usuario = request.user
		viaje = Viaje.objects.get(id=id)
		par1 = Parada.objects.get(id=origen)
		par2 = Parada.objects.get(id=destino)

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
		
		print(id)
		print(origen)
		print(destino)

		if request.POST.get("plaza1"): print(request.POST.get("plaza1"))
		if request.POST.get("plaza2"): print(request.POST.get("plaza2"))
		if request.POST.get("plaza3"): print(request.POST.get("plaza3"))
		if request.POST.get("plaza4"): print(request.POST.get("plaza4"))
		print("--------------------------------------")
	return render(request, 'Buscar_Management/correcto.html')