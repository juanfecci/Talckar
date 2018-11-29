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

'''
def BuscarDetail(request, pk, origen, destino):
	if request.method == "POST":
		print("Wena wena ------------------")
	else:
		print("wea asdasdasd sddddddddddddddddddd")
		return render(request, "Buscar_Management/buscar_detail.html", {'viaje': Viaje.objects.get(pk)})
'''
class BuscarDetail(DetailView):
	model = Viaje
	template_name = "Buscar_Management/buscar_detail.html"

def Error(request):
	if request.method =="Error":
		form = BuscarForm(request.POST)
		return render(request, 'Buscar_Management/buscar.html', {'form': form} )
