# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Core.models import *
from Asset_Management.ASE_Core.models import *

class Scan(models.Model):
	startDate = models.DateTimeField(max_length=15,   null=True, blank=True, auto_now_add=True)
	finishDate = models.DateTimeField(max_length=15, null=True, blank=True)

	proxy = models.BooleanField(default = False)

	proxyHttp = models.CharField(max_length=20, null=True, default="-1", blank=True)
	proxyHttpPort = models.CharField(max_length=10, null=True, default="-1", blank=True)
	proxySsl = models.CharField(max_length=20, null=True, default="-1", blank=True)
	proxySslPort = models.CharField(max_length=10, null=True, default="-1", blank=True)
	proxyFtp = models.CharField(max_length=20, null=True, default="-1", blank=True)
	proxyFtpPort = models.CharField(max_length=10, null=True, default="-1", blank=True)
	proxySocks = models.CharField(max_length=20, null=True, default="-1", blank=True)
	proxySocksPort = models.CharField(max_length=10, null=True, default="-1", blank=True)
	
	name = models.CharField(max_length=50, null=True, default="0")
	task = models.OneToOneField(Task,null=True, blank=True, related_name='scan')
	
	assets = models.ManyToManyField(Asset)


	class Meta:
		verbose_name = "Scan"
		verbose_name_plural = "Scans"

	def __unicode__(self):
		return str(self.name)

class Finding(models.Model):
	asset = models.ForeignKey(Asset, on_delete=models.CASCADE, default=None, related_name='vim_finding', null=True)
	scan = models.ForeignKey(Scan, on_delete=models.CASCADE, default=None, related_name='vim_finding')
	url = models.CharField(max_length=50, null=True)

	title = models.CharField(max_length=50, null=True)
	port = models.CharField(max_length=50, null=True)
	statusCode = models.CharField(max_length=50, null=True)
	status = models.CharField(max_length=50, null=True)

	image = models.ImageField(upload_to='')

	class Meta:
		verbose_name = "Finding"
		verbose_name_plural = "Findings"

	def __unicode__(self):
		return str(self.asset) + str(self.port) + str(self.title)



