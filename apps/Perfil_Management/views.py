# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from Core.models import *
#from form import *

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from forms import PerfilEditForm
from forms import UploadImageForm
from forms import VehiculoEditForm
from forms import UploadCarImageForm
from django.shortcuts import get_object_or_404
from flask import Flask, render_template, request, redirect

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext as _

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            request.user.save()
            update_session_auth_hash(request, form.user)  # Important!
            messages.success(request, _('Tu contraseña se cambio con exito!'))
            return render(request, 'Perfil_Management/pass_change.html', {'redirectt': True})
        else:
            messages.error(request, _('Por favor corrige tus errores'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Perfil_Management/pass_change.html', {'form': form})

def PerfilDetail(request, pk):
	user = User.objects.get(id = pk)
	return render(request, "Perfil_Management/perfil_detail2.html", {'usuario': user, 'flag': False})

def inicio(request):
	return render(request, "base.html", {});

def EditarPerfil(request):
	print("hola mundo")
	if (request.method == "POST"):
		form = PerfilEditForm(request.POST)
		#form2 = UploadImageForm(request.POST, request.FILES)
		if (form.is_valid()):
			print("dentro del form is valid")
			#nuevoPerfil = form.save(commit = False)
			request.user.first_name = request.POST.get('first_name')
			request.user.last_name = request.POST.get('last_name')
			request.user.correo = request.POST.get('email')
			request.user.profesion = request.POST.get('profesion')
			request.user.interes = request.POST.get('interes')
			request.user.fumador = request.POST.get('fumador')
			request.user.celular = request.POST.get('celular')
			#request.user.foto = form2.cleaned_data['foto']
			request.user.save()
			return render(request, "base.html", {'user': request.user})
		return render(request, "Perfil_Management/perfil_detail3.html", {'errores': form.errors})
	form = PerfilEditForm()
	#form2 = UploadImageForm()
	return render(request, "Perfil_Management/perfil_edit2.html", {'form': form})

def EditarFoto(request):
	if (request.method == "POST"):
		form = UploadImageForm(request.POST, request.FILES)
		if (form.is_valid()):
			request.user.foto = form.cleaned_data['foto']
			request.user.save()
			return render(request, "base.html", {'user': request.user})
	form = UploadImageForm()
	return render(request, "Perfil_Management/perfil_image_edit.html", {'form': form})

class PerfilEdit(DetailView):
	model = User
	template_name = "Perfil_Management/perfil_edit.html"

def EditarVehiculo(request):
	if (request.method == "POST"):
		form = VehiculoEditForm(request.POST)
		if (form.is_valid()):
			datos = form.save(commit = False)
			request.user.datos_conductor.vehiculo.marca = datos.marca
			request.user.datos_conductor.vehiculo.modelo = datos.modelo
			request.user.datos_conductor.vehiculo.color = datos.color
			request.user.datos_conductor.vehiculo.anno = datos.anno
			request.user.datos_conductor.vehiculo.numero_asientos = datos.numero_asientos
			request.user.datos_conductor.vehiculo.precio_combustible = datos.precio_combustible
			request.user.datos_conductor.vehiculo.save()
			request.user.save()
			return render(request, "base.html", {'user': request.user})
	form = VehiculoEditForm()
	return render(request, "Perfil_Management/vehiculo_edit.html", {'form': form})

def EditarFotoVehiculo(request):
	if (request.method == "POST"):
		form = UploadCarImageForm(request.POST, request.FILES)
		if (form.is_valid()):
			request.user.datos_conductor.vehiculo.foto_vehiculo = form.cleaned_data['foto_vehiculo']
			request.user.datos_conductor.vehiculo.save()
			request.user.save()
			return render(request, "base.html", {'user': request.user})
	form = UploadCarImageForm()
	return render(request, "Perfil_Management/vehiculo_image_edit.html", {'form': form})

def VerPerfil(request, pk):
	user = User.objects.get(id = pk)
	num_vals = len(user.valoraciones.all())
	if (num_vals >= 3):
		valoraciones = user.valoraciones.all().order_by('-id')[:3]
		print("valoraciones: ", user.valoraciones)
		return render(request, "Perfil_Management/perfil_detail2.html", {'usuario': user, 'flag': False, 'valoraciones': valoraciones, 'n': num_vals})
	else:
		valoraciones = user.valoraciones.all().order_by('-id')[:num_vals]
		return render(request, "Perfil_Management/perfil_detail2.html", {'usuario': user, 'flag': False, 'valoraciones': valoraciones, 'n': num_vals})


def MasValoraciones(request, pk):
	user = User.objects.get(id = pk)
	return render(request, "Perfil_Management/valoraciones_detail.html", {'valoraciones': user.valoraciones})

def DetalleVehiculo(request, pk):
	user = User.objects.get(id = pk)
	conductor = user.datos_conductor
	return render(request, "Perfil_Management/vehiculo_detail.html", {'conductor': conductor})

def getValor(conductor):
	vals = conductor.first().valoraciones.all()
	suma = 0.0
	for val in vals:
		suma += val.puntaje

	if len(vals) == 0:
		return "5.0"
	return "{0:.2f}".format(suma/len(vals))

def Valorar(request, pk, tipo, reserva_id, usuario_id):
	viaje = Viaje.objects.get(id=pk)
	reservas = Reserva.objects.filter(viaje=pk).filter(estado=2)
	if tipo == "Fin":
		for r in reservas:
			r.estado = 1
			r.save()
		viaje.estado = 1
		viaje.save()
		return render(request, 'Perfil_Management/completado2.html', {'tipo': tipo})

	if len(reservas) == 0:
		viaje.estado = 1
		viaje.save()
		return render(request, 'Perfil_Management/completado2.html', {'tipo': tipo})

	if (tipo == 'Conductor'):
		#trayectos = Trayecto.objects.filter(viaje=pk).filter(estado=2)
		return render(request, 'Perfil_Management/seleccionar.html', {'viaje':viaje, 'reservas':reservas, 'tipo':'Fin'})
	elif (tipo == 'Pasajero'):
		reserva = Reserva.objects.get(id = reserva_id)
		conductor = viaje.user
		aux = str(getValor(conductor))
		print(aux)
		#conductor = viaje.conductor
		return render(request, 'Perfil_Management/valorar_conductor.html', {'viaje': viaje, 'reserva': reserva, 'conductor': conductor, 'valor': aux})

def ValorarPasajero(request, viaje_id, reserva_id):	
	viaje = Viaje.objects.get(id=viaje_id)
	usuario = viaje.user.first()

	val = Valoracion()
	estrella = request.POST.get("estrellas")
	
	if estrella == "5": val.puntaje = 5
	elif estrella == "4": val.puntaje = 4
	elif estrella == "3": val.puntaje = 3
	elif estrella == "2": val.puntaje = 2
	elif estrella == "1": val.puntaje = 1

	comentario = request.POST.get("Comentario")
	val.comentario = comentario

	val.save()
	usuario.valoraciones.add(val)
	usuario.save()

	reserva = Reserva.objects.get(id=reserva_id)
	reserva.estado = 1
	reserva.save()
	return Valorar(request, viaje_id, 'Pasajero', reserva_id, usuario.id)

def ValorarConductor(request, viaje_id, reserva_id):
	
	viaje = Viaje.objects.get(id=viaje_id)
	reserva = Reserva.objects.get(id = reserva_id)
	usuario = reserva.user.first()

	if request.method == "POST" and reserva.estado != 2:

		val = Valoracion()
		estrella = request.POST.get("estrellas")
		
		if estrella == "5": val.puntaje = 5
		elif estrella == "4": val.puntaje = 4
		elif estrella == "3": val.puntaje = 3
		elif estrella == "2": val.puntaje = 2
		elif estrella == "1": val.puntaje = 1

		comentario = request.POST.get("Comentario")
		val.comentario = comentario

		val.save()
		usuario.valoraciones.add(val)
		usuario.save()

		reserva = Reserva.objects.get(id=reserva_id)
		reserva.estado = 1
		reserva.save()
		return Valorar(request, viaje_id, 'Conductor', reserva_id, usuario.id)
	else:
		reserva.estado = 3
		reserva.save()
		aux = str(getValor(reserva.user))
		print(aux)
		#conductor = viaje.conductor
		return render(request, 'Perfil_Management/valorar_pasajero.html', {'viaje': viaje, 'reserva': reserva, 'pasajero': reserva.user, 'valor': aux})
