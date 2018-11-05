# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Core.models import *

# Create your models here.


class Tag(models.Model):
	code = models.CharField(max_length=50, null=True)
	tag = models.CharField(max_length=50, null=True)
	
	class Meta:
		verbose_name = "Tag"
		verbose_name_plural = "Tag"

	def __unicode__(self):
		return str(self.tag) + "-" + str(self.code)

class Asset(models.Model):
	address = models.CharField(max_length=50, null=True)
	tags = models.ManyToManyField("Tag", blank=True, related_name="Assets")

	class Meta:
		verbose_name = "Asset"
		verbose_name_plural = "Assets"

	def __unicode__(self):
		return str(self.address)
