# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from django.contrib.auth.decorators import login_required

import Core.worker_master 

from Core.models import *

import json

@login_required()
def home(request):
	#try: Core.worker_master.vigilant.apply_async()
	#except: print "The vigilant don't start"
	usuario = request.user
	viaje = usuario.viajes.filter(estado=2)

	if len(viaje) == 0:
		return render(request,'base.html',{})	

	else:
		viaje = viaje.first()
		return render(request,'base2.html',{'viaje':viaje})	

def AdministrarViaje(request, pk):
	viaje = Viaje.objects.get(id=pk)
	trayectos = Trayecto.objects.filter(viaje=pk).filter(estado=1)

	primero = trayectos.first()
	trayectos = trayectos.exclude(id=primero.id)

	return render(request, 'administrar.html', {'viaje':viaje, 'trayectos':trayectos, 'primero':primero})

def updateTask(request, id, status, percent):
	print id, status, percent
	task = Task.objects.get(task_id=id)
	task.status = status
	if percent == "-1" and status=="SUCCESS": task.percent = task.total
	elif percent == "-1" and status=="WAITING": task.percent = "0"
	else: task.percent = percent
	task.save()

def taskList(request):
	tasks = Task.objects.exclude(status__in = ["FAILURE", "UPLOADING"])
	msg = []
	for task in tasks:
		if task.task_type == "Visibility":
			try:
				msg.append([task.task_id, task.task_type, [task.scan.proxy]])
			except:
				msg.append([task.task_id, task.task_type, []])

	print msg
	msg = json.dumps(msg)
	return HttpResponse(msg)

@login_required()
def changeActiveClient(request,clientId):
	id_client = clientId

	user = request.user

	if user.clients.filter(id=id_client) > 0:
		user.activeClient = user.clients.filter(id=id_client)[0]
		user.save()
	return redirect(home)
