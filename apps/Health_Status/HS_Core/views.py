# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings

from models import *

import datetime

import requests

# Create your views here.


def CRON():
	check_sites()


def check_sites():
	#Get sites to check
	now = datetime.datetime.now().strftime('%M')
	now = int(now)

	sites = Site.objects.all()
	for site in sites:
		if now % site.interval == 0:
			newBeat = HeartBeat()
			newBeat.site = site
			newBeat.date = datetime.datetime.now()
			content = True
			status = True
			try:
				r = requests.get(site.url,stream=False)
				roundtrip = r.elapsed.total_seconds()
			except:
				newBeat.responseTime = None
				newBeat.status = 'DOWN'
			else:
				newBeat.status = 'DOWN'
				if site.textResponse not in (None, ""):
					if site.textResponse not in unicode(r.content, "utf-8"):
						content = False
				if int(r.status_code) != int(site.statusCode):
					status = False
				if status and content:
					newBeat.status = "UP"
				else:
					newBeat.status = "CONF"
				newBeat.responseTime = roundtrip*1000
			print newBeat, newBeat.status, status,content
			newBeat.save()
	return

def dashboard(request):

	return render(request, 'Health_Status/dashboard.html',{})