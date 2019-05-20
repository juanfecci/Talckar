# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	clients = models.ManyToManyField("Client")
	activeClient = models.ForeignKey("Client",related_name="UsersViewing", null=True, blank=True)
	datos_conductor = models.ForeignKey("Conductor",related_name="DatosConductor", null=True, blank=True)
	correo = models.CharField(max_length=30,null=False, default=" ")

	profesion = models.CharField(max_length=30,null=False, default=" ")
	interes = models.CharField(max_length=30,null=False, default=" ")
	fumador = models.CharField(max_length=30,null=False, default=" ")	
	celular = models.IntegerField(default=123456789)

	foto = models.ImageField(upload_to='user', default="default.png")

	viajes = models.ManyToManyField("Viaje", related_name="user")
	trayectos = models.ManyToManyField("Trayecto", related_name="user") #Por eliminar
	reserva = models.ManyToManyField("Reserva", related_name="user")	

	class Meta:
		verbose_name = "User"
		verbose_name_plural = "Users"

	def __unicode__(self):
		return self.username

class Client(models.Model):
	name = models.CharField(max_length=15,null=False)
	description = models.TextField(max_length=200,null=False)
	modules = models.ManyToManyField("Module")

	class Meta:
		verbose_name = "Client"
		verbose_name_plural = "Clients"

	def __unicode__(self):
		return self.name	

	
class Module(models.Model):
	name = models.CharField(max_length=30,null=False)
	pathToTemplate = models.CharField(max_length=50,null=False)
	description = models.TextField(max_length=200,null=False)
	
	class Meta:
		verbose_name = "Module"
		verbose_name_plural = "Modules"

	def __unicode__(self):
		return self.name

SCAN_STATUS_CHOICES = (
	("WT", 'En espera'),
	("PA", "Pausado"),
	("RU", "Corriendo"),
	("SC", "Terminado"),
	("ER", "Error"),
	)

# Falta eliminar parametros
class Conductor(models.Model):
	licencia = models.CharField(max_length=30,null=False)
	fecha_obtencion = models.CharField(max_length=30,null=False)
	marca = models.CharField(max_length=30,null=False) #Por eliminar
	modelo = models.CharField(max_length=30,null=False) #Por eliminar
	foto_vehiculo = models.ImageField(upload_to='autos') #Por eliminar

	class Meta:
		verbose_name = "Conductor"
		verbose_name_plural = "Conductores"

	def __unicode__(self):
		return self.modelo

# Falta agregarlo al sistema
class Vehiculo(models.Model):
	marca = models.CharField(max_length=30,null=False)
	modelo = models.CharField(max_length=30,null=False)
	foto_vehiculo = models.ImageField(upload_to='autos')
	color = models.CharField(max_length=15,null=False)
	anno = models.IntegerField(null=True, blank=True, default=1800)
	numero_asientos = models.IntegerField(null=True, blank=True, default=4)
	precio_combustible = models.IntegerField(null=True, blank=True, default=30)

	class Meta:
		verbose_name = "Vehiculo"
		verbose_name_plural = "Vehiculos"

	def __unicode__(self):
		return self.marca + " " + self.modelo

# Falta eliminar parametros
class Viaje(models.Model):
	tarifaPreferencias = models.IntegerField(null=False,blank=True, default=100)
	maletero = models.BooleanField(default=True) #Por eliminar
	mascota = models.BooleanField(default=True) #Por eliminar
	paradas = models.ManyToManyField("Parada")
	plazas_max = models.IntegerField(null=False,blank=False, default=4) #Por eliminar
	origen = models.ForeignKey("Parada",related_name="ParadaOrigen", null=False, default = 1)
	destino = models.ForeignKey("Parada",related_name="ParadaDestino", null=False, default = 1)
	origen = models.ForeignKey("Parada",related_name="ParadaOrigen", null=False, default = 1)
	prestacion = models.ForeignKey("Prestacion",related_name="Prestacion", null=False, default = 1) #Falta aplicarlo
	estado =  models.IntegerField(default = -1)
	#-1 En espera
	# 0 Realizando viaje
	# 1 Viaje Terminado
	# 2 Viaje cercano
	precio =  models.IntegerField(default = 100)


	class Meta:
		verbose_name = "Viaje"
		verbose_name_plural = "Viajes"

	def __unicode__(self):
		return self.origen.nombre + " " + self.destino.nombre

	def verificar(self, cordx1, cordy1, cordx2, cordy2, fecha):
		p1 = self.paradas.filter(coordenada_x__gte=cordx1-1).filter(coordenada_x__lte=cordx1+1).filter(coordenada_y__gte=cordy1-1).filter(coordenada_y__lte=cordy1+1)
		if p1.exists():
			p2 = self.paradas.filter(coordenada_x__gte=cordx2-1).filter(coordenada_x__lte=cordx2+1).filter(coordenada_y__gte=cordy2-1).filter(coordenada_y__lte=cordy2+1)
			if p2.exists():
				return (p1.first(), p2.first())
		return (-1, -1)
		#return self.paradas.filter(coordenada_x__gte=cordx1-1).filter(coordenada_x__lte=cordx1+1).filter(coordenada_y__gte=cordy1-1).filter(coordenada_y__lte=cordy1+1).exists() and self.paradas.filter(coordenada_x__gte=cordx2-1).filter(coordenada_x__lte=cordx2+1).filter(coordenada_y__gte=cordy2-1).filter(coordenada_y__lte=cordy2+1).exists()

# Falta agregarlo al sistema
class Prestacion(models.Model):
	max_plazas = models.IntegerField(null=False,blank=False, default=4)
	maletero = models.BooleanField(default=True)
	mascota = models.BooleanField(default=True)
	silla_ninnos = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Prestacion"
		verbose_name_plural = "Prestaciones"

	def __unicode__(self):
		return str(self.max_plazas)

class Parada(models.Model):
	nombre = models.CharField(max_length=30,null=False, default = "Concepcion")
	coordenada_x = models.FloatField(null=True,blank=True)
	coordenada_y = models.FloatField(null=True,blank=True)
	hora = models.CharField(max_length=30,null=False, default = "15:00")
	fecha = models.CharField(max_length=30,null=False, default = "2018/11/12")

	class Meta:
		verbose_name = "Parada"
		verbose_name_plural = "Paradas"

	def __unicode__(self):
		return self.nombre

# Clase completa por eliminar
class Trayecto(models.Model):
	precio = models.IntegerField(null=True,blank=True)
	origen = models.ForeignKey("Parada",related_name="ParadaOrigenTrayecto", null=False, blank=True, default=1)
	destino = models.ForeignKey("Parada",related_name="ParadaDestinoTrayecto", null=False, blank=True, default=1)
	plazas = models.ManyToManyField("Plaza")
	estado =  models.IntegerField(default = -1)
	#-1 en espera
	# 0 cancelado
	# 1 aceptado 
	# 2 terminado
	viaje = models.ForeignKey("Viaje",related_name="Viaje", null=False, blank=True, default=1)
	
	class Meta:
		verbose_name = "Trayecto"
		verbose_name_plural = "Trayectos"

	def __unicode__(self):
		return self.origen.nombre + " " + self.destino.nombre

# Falta reemplazarla por Trayecto
class Tramo(models.Model):
	km = models.IntegerField(null=True,blank=True)
	precio = models.IntegerField(null=True,blank=True)
	origen = models.ForeignKey("Parada",related_name="ParadaOrigenTramo", null=False, blank=True, default=1)
	destino = models.ForeignKey("Parada",related_name="ParadaDestinoTramo", null=False, blank=True, default=1)
	plazas = models.ManyToManyField("Plaza")
	
	viaje = models.ForeignKey("Viaje",related_name="ViajeTramo", null=False, blank=True, default=1)
	
	class Meta:
		verbose_name = "Trayecto"
		verbose_name_plural = "Trayectos"

	def __unicode__(self):
		return self.origen.nombre + " " + self.destino.nombre

# Falta implememtarla al sistema
class Reserva(models.Model):
	posicion = models.IntegerField(null=True,blank=True)
	estado =  models.IntegerField(default = -1)
	tramo = models.ForeignKey("Tramo",related_name="Tramo", null=False, blank=True, default=1)
	#-1 en espera
	# 0 cancelado
	# 1 aceptado 
	# 2 terminado

	class Meta:
		verbose_name = "Plazas"
		verbose_name_plural = "Plazas"

	def __unicode__(self):
		return str(self.posicion) + " " + str(self.estado)

# Clase por eliminar
class Plaza(models.Model):
	posicion = models.IntegerField(null=True,blank=True)
	caracteristica = models.CharField(max_length=30,null=False)

	class Meta:
		verbose_name = "Plazas"
		verbose_name_plural = "Plazas"

	def __unicode__(self):
		return str(self.posicion)

class Valoracion(models.Model):
	puntaje = models.IntegerField(null=True,blank=True)
	comentario = models.CharField(max_length=200,null=False)

	class Meta:
		verbose_name = "Valoracion"
		verbose_name_plural = "Valoraciones"

	def __unicode__(self):
		return str(self.puntaje)