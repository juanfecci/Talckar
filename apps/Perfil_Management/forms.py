from django import forms
from django.forms import widgets
from models import *
from Core.models import *


class PerfilEditForm(forms.ModelForm):
    fumador = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'False'), (True, 'True')),
                   widget=forms.RadioSelect, 
                   initial = False)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'profesion', 'interes', 'fumador', 'celular')

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('foto',)

class UploadCarImageForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('foto_vehiculo',)

class VehiculoEditForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('marca', 'modelo', 'color', 'anno', 'numero_asientos', 'precio_combustible')