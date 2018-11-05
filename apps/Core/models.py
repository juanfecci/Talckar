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

	viajes = models.ManyToManyField("Viaje")

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
	id_viaje = models.IntegerField(null=True,blank=True)
	tarifaPreferencias = models.IntegerField(null=True,blank=True)
	maletero = models.BooleanField(default=True)
	mascota = models.BooleanField(default=True)
	paradas = models.ManyToManyField("Parada")
	trayectos = models.ManyToManyField("Trayecto")
	fecha = models.CharField(max_length=30,null=False, default="21/10/18")
	hora = models.CharField(max_length=30,null=False, default="15:00")
	origen = models.ForeignKey("Parada",related_name="ParadaOrigen", null=True, blank=True)
	destino = models.ForeignKey("Parada",related_name="ParadaDestino", null=True, blank=True)


	class Meta:
		verbose_name = "Viaje"
		verbose_name_plural = "Viajes"

	def __unicode__(self):
		return str(self.id_viaje)

class Parada(models.Model):
	id_parada = models.IntegerField(null=True,blank=True)
	nombre = models.CharField(max_length=30,null=False, default = "Concepcion")
	coordenada_x = models.IntegerField(null=True,blank=True)
	coordenada_y = models.IntegerField(null=True,blank=True)
	hora = models.CharField(max_length=30,null=False, default = "15:00")
	fecha = models.CharField(max_length=30,null=False, default = "21/10/18")

	class Meta:
		verbose_name = "Parada"
		verbose_name_plural = "Paradas"

	def __unicode__(self):
		return self.nombre

class Trayecto(models.Model):
	id_trayecto = models.IntegerField(null=True,blank=True)
	precio = models.IntegerField(null=True,blank=True)
	origen = models.ForeignKey("Parada",related_name="ParadaOrigenTrayecto", null=True, blank=True)
	destino = models.ForeignKey("Parada",related_name="ParadaDestinoTrayecto", null=True, blank=True)
	plazas = models.ManyToManyField("Plaza")
	
	class Meta:
		verbose_name = "Trayecto"
		verbose_name_plural = "Trayectos"

	def __unicode__(self):
		return str(self.id_trayecto)

class Plaza(models.Model):
	id_plaza = models.IntegerField(null=True,blank=True)
	posicion = models.IntegerField(null=True,blank=True)
	mascota = models.BooleanField(default=True)
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