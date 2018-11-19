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

