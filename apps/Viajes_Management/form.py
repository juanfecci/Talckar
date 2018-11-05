from django import forms
from django.forms import widgets
from models import *
from Core.models import *

class ViajeForm(forms.Form):

	origen = forms.CharField(label = "Origen")
	mapa1 = forms.CharField(widget=forms.Textarea, required=False)
	fecha_inicio = forms.CharField(label = "Fecha de inicio (DD/MM/YY HH:MM)")
	destino = forms.CharField(label = "Destino")
	mapa2 = forms.CharField(widget=forms.Textarea, required=False)
	fecha_final = forms.CharField(label = "Fecha de llegada (DD/MM/YY HH:MM)")

	paradas = forms.CharField(widget=forms.Textarea, label = "Paradas (Nombre YY/MM/DD HH:MM:SS)")

	tarifa = forms.IntegerField(label="Tarifa")
	maletero  = forms.BooleanField(label = "Maletero", required=False)
	mascota = forms.BooleanField(label = "Mascota", required=False)