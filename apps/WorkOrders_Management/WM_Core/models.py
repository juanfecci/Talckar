# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Core.models import *
# Create your models here.

SERVICES_CHOICES = (
	('VM', 'Vulnerabilidades'),
	("TM", "Amenazas"),
	("CM", "Certificados"),
	("IN", "Incidentes"),
	("EV", "Eventos"),
	("HD", "Hardening"),
	("PC", "Parches"),
	("GC", "Gestion CCI"),
	("ID", "Gestion Identidades"),
	)

class Ticket(models.Model):
	id_petition = models.CharField(max_length=15, null=True)
	id_workOrder = models.CharField(max_length=15, null=False, unique=True)

	client = models.CharField(max_length=50, null=True)
	resume = models.CharField(max_length=50, null=True)
	notes = models.CharField(max_length=500, null=True)

	user_asigned = models.CharField(max_length=15, null=True)
	group_asigned = models.CharField(max_length=15, null=True)

	status = models.CharField(max_length=20, null=True)
	status_cause = models.CharField(max_length=20, null=True)
	status_note = models.CharField(max_length=500, null=True)
	created = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name = "Ticket"
		verbose_name_plural = "Tickets"

	def __unicode__(self):
		return self.id_workOrder


class Log(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=None)
	date = models.DateTimeField(auto_now=False, null=True)
	user = models.CharField(max_length=15, null=False)

	method = models.CharField(max_length=15, null=False)
	event = models.CharField(max_length=15, null=False)
	message = models.CharField(max_length=15, null=False)


	class Meta:
		verbose_name = "Log"
		verbose_name_plural = "Logs"

	def __unicode__(self):
		return self.ticket.id_workOrder + " " + str(self.date) + " " + self.user


class Detail(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=None)

	id_detail = models.CharField(max_length=15, default="")
	type = models.CharField(max_length=15, default="")
	title = models.CharField(max_length=15, default="")
	comment = models.CharField(max_length=15, default="")
	files = models.CharField(max_length=15, default="")
	date = models.DateTimeField(max_length=15, default="")
	forwarder = models.CharField(max_length=15, default="")

	class Meta:
		verbose_name = "Detail"
		verbose_name_plural = "Details"

	def __unicode__(self):
		return self.ticket.id_workOrder 


class Following(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, default=None)
	wo = models.CharField(max_length=15, default="")
	last_escaling = models.CharField(max_length=15, default="")
	active = models.BooleanField(default=False)
	service = models.CharField(choices=SERVICES_CHOICES,max_length=50, null=True)

	class Meta:
		verbose_name = "Following"
		verbose_name_plural = "Followings"

	def __unicode__(self):
		return self.wo + " " + self.last_escaling

class Comentary(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, default=None)
	author = models.ForeignKey(User, null=True, default=None)
	comment = models.CharField(max_length=300, default="")
	date = models.DateTimeField(auto_now=True, null=True)

	class Meta:
		verbose_name = "Comentary"
		verbose_name_plural = "Comentaries"

	def __unicode__(self):
		return self.ticket.id_workOrder + " " + str(self.date)

ESCALATION_METHOD_CHOICES = (
	('TL', 'Telefono'),
	("EM", "Email"),
	("PP", "En Persona"),
	)

class Escalation(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, default=None)
	author = models.ForeignKey(User, null=True, default=None)
	method = models.CharField(choices=ESCALATION_METHOD_CHOICES, max_length=300, default="")
	recipient = models.CharField(max_length=300, default="")
	comment = models.CharField(max_length=300, default="")
	date = models.DateTimeField(auto_now=True, null=True)

	class Meta:
		verbose_name = "Escalation"
		verbose_name_plural = "Escalations"

	def __unicode__(self):
		return self.ticket.id_workOrder + " " + str(self.date)



class Inbox(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=None)
	date_in = models.DateTimeField(auto_now=False, null=True)
	date_out = models.DateTimeField(auto_now=False,null=True)
	active = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Inbox"
		verbose_name_plural = "Inboxs"

	def __unicode__(self):
		return self.ticket.id_workOrder + " " + str(self.date_in) + " " + str(self.active)
