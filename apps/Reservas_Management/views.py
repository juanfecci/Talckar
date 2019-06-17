# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Core.models import *

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import get_object_or_404

def getValor(conductor):
	vals = conductor.valoraciones.all()
	suma = 0.0
	for val in vals:
		suma += val.puntaje
	if len(vals) == 0:
		return 0
	return "{0:.2f}".format(suma/len(vals))


class ReservaList(ListView):
	model = Reserva
	template_name = "Reservas_Management/reserva_list.html"
	def get_queryset(self):
		for user in User.objects.all():
			user.promedioVal = getValor(user)
			user.save()
		return self.request.user.reservas.all()

class ReservaDetail(DetailView):
	model = Reserva
	template_name = "Reservas_Management/reserva_detail.html"

def ReservaDelete(request, reserva_id):
	Reserva.objects.filter(id=reserva_id).delete()
	print(reserva_id)
	return render(request, 'Reservas_Management/correcto.html')