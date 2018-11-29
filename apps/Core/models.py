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

	foto = models.ImageField(upload_to='user', default="default.png")

	viajes = models.ManyToManyField("Viaje", related_name="user")
	trayectos = models.ManyToManyField("Trayecto")

	celular = models.IntegerField(default=123456789)

	class Meta:
		verbose_name = "User"
		verbose_name_plural = "Users"

	def __unicode__(self):
		return self.username

class Client(models.Model):
	name = models.CharField(max_length=15,null=False)
	description = models.TextField(max_length=200,null=False)
	modules = models.ManyToManyField("Module")
	workers = models.ManyToManyField("Worker")

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

class Task(models.Model):
	task_id = models.CharField(max_length=30,null=False)
	previus_id = models.CharField(max_length=30,null=False)
	task_type = models.CharField(max_length=30,null=False)
	status = models.CharField(choices=SCAN_STATUS_CHOICES, max_length=300, default="WT")
	percent = models.CharField(max_length=50, null=True, default="0")
	total = models.CharField(max_length=50, null=True, default="0")

	class Meta:
		verbose_name = "Task"
		verbose_name_plural = "Task"

	def __unicode__(self):
		return str(self.task_type) + " " + str(self.task_id)

class Worker(models.Model):
	name = models.CharField(max_length=30,null=False)
	tasks = models.ManyToManyField("Task", blank=True)

	class Meta:
		verbose_name = "Worker"
		verbose_name_plural = "Worker"

	def __unicode__(self):
		return self.name

class Conductor(models.Model):
	licencia = models.CharField(max_length=30,null=False)
	fecha_obtencion = models.CharField(max_length=30,null=False)
	marca = models.CharField(max_length=30,null=False)
	modelo = models.CharField(max_length=30,null=False)
	foto_vehiculo = models.ImageField(upload_to='autos')

	class Meta:
		verbose_name = "Conductor"
		verbose_name_plural = "Conductores"

	def __unicode__(self):
		return self.modelo

class Viaje(models.Model):
	#id_viaje = models.IntegerField(null=True,blank=True)
	tarifaPreferencias = models.IntegerField(null=False,blank=True, default=100)
	maletero = models.BooleanField(default=True)
	mascota = models.BooleanField(default=True)
	paradas = models.ManyToManyField("Parada")
	#trayectos = models.ManyToManyField("Trayecto")
	#fecha = models.DateField(max_length=30,null=False, default="2018-11-12")
	#hora = models.CharField(max_length=30,null=False, default="15:00")
	origen = models.ForeignKey("Parada",related_name="ParadaOrigen", null=False, default = 1)
	destino = models.ForeignKey("Parada",related_name="ParadaDestino", null=False, default = 1)
	estado =  models.IntegerField(default = -1)


	class Meta:
		verbose_name = "Viaje"
		verbose_name_plural = "Viajes"

	def __unicode__(self):
		return self.origen.nombre + " " + self.destino.nombre

class Parada(models.Model):
	#id_parada = models.IntegerField(null=True,blank=True)
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

class Trayecto(models.Model):
	#id_trayecto = models.IntegerField(null=True,blank=True)
	precio = models.IntegerField(null=True,blank=True)
	origen = models.ForeignKey("Parada",related_name="ParadaOrigenTrayecto", null=False, blank=True, default=1)
	destino = models.ForeignKey("Parada",related_name="ParadaDestinoTrayecto", null=False, blank=True, default=1)
	plazas = models.ManyToManyField("Plaza")
	estado =  models.IntegerField(default = -1)
	viaje = models.ForeignKey("Viaje",related_name="Viaje", null=False, blank=True, default=1)
	
	class Meta:
		verbose_name = "Trayecto"
		verbose_name_plural = "Trayectos"

	def __unicode__(self):
		return self.origen.nombre + " " + self.destino.nombre

class Plaza(models.Model):
	#id_plaza = models.IntegerField(null=True,blank=True)
	posicion = models.IntegerField(null=True,blank=True)
	caracteristica = models.CharField(max_length=30,null=False)

	class Meta:
		verbose_name = "Plazas"
		verbose_name_plural = "Plazas"

	def __unicode__(self):
		return str(self.posicion)


class Demo(models.Model):
	id_plaza = models.IntegerField(null=True,blank=True)

	class Meta:
		verbose_name = "Demo"
		verbose_name_plural = "Demos"

	def __unicode__(self):
		return str(self.id_plaza)

class Valoracion(models.Model):
	puntaje = models.IntegerField(null=True,blank=True)
	comentario = models.CharField(max_length=200,null=False)

	class Meta:
		verbose_name = "Valoracion"
		verbose_name_plural = "Valoraciones"

	def __unicode__(self):
		return str(self.puntaje)