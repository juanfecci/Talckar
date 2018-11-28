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

class TrayectoList(ListView):
	model = Trayecto
	template_name = "Trayectos_Management/trayecto_list.html"
	def get_queryset(self):
		return self.request.user.trayectos.all()

class TrayectoDetail(DetailView):
	model = Trayecto
	template_name = "Trayectos_Management/trayecto_detail.html"