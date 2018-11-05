from django import forms
from django.forms import widgets
from models import *
from Core.models import *

class BuscarForm(forms.Form):

	origen = forms.CharField(label = "Origen")
	destino = forms.CharField(label = "Destino")
	fecha = forms.CharField(label = "Fecha (DD/MM/YY)")
	