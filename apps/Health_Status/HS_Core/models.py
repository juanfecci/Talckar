# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Site(models.Model):
	name = models.CharField(max_length=15, null=False)
	url = models.CharField(max_length=300, null=False)
	STATUS_CODE = (
	    ('404', '404 - Not found'),
	    ('200', '200 - OK'),
	    ('302', '302 - Redirect'),
	)
	statusCode = models.CharField(max_length=3, null=False, choices=STATUS_CODE)
	textResponse = models.TextField(max_length=1000, null=True, blank=True)
	TIMES = (
		(1,'1 minuto'),
		(3,'3 minutos'),
		(5,'5 minutos'),
		(10,'10 minutos'),
		(15,'15 minutos'),
		(30,'30 minutos'),
	)
	interval = models.IntegerField(null=True,blank=True, choices=TIMES)

	class Meta:
		verbose_name = "Site"
		verbose_name_plural = "Sites"

	def __unicode__(self):
		return self.name + " " + self.url	

class HeartBeat(models.Model):
	STATUS = (
		('UP','Arriba'),
		('CONF','Conflicto'),
		('DOWN','Abajo'),
	)
	status = models.CharField(max_length=3, null=False, choices=STATUS)
	date = models.DateField(auto_now_add=True)
	responseTime = models.IntegerField(null=True,blank=True)
	site = models.ForeignKey("Site",related_name="Site", null=False)

	class Meta:
		verbose_name = "HeartBeat"
		verbose_name_plural = "HeartBeats"

	def __unicode__(self):
		return self.site.name + " " + str(self.date	)


class Notification(models.Model):
	pass