# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *
from form import *
import socket, time, os, base64


# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import get_object_or_404

import Core.worker_slave

class ScanList(ListView):
	model = Scan
	template_name = "Visibility_Management/scans_list.html"

def ScanCreate(request):
	client = request.user.activeClient

	if request.method == "POST":
		form = ScanForm(request.POST)
		form.fields['workers'].queryset = request.user.activeClient.workers.all()

		if form.is_valid():
			name = form.cleaned_data['name']
			
			assets = form.cleaned_data['assets'].split("\n")
			
			workers = form.cleaned_data['workers']
			
			StartScan(name, workers, assets, form.cleaned_data['proxy']
				, form.cleaned_data['proxyHttp'], form.cleaned_data['proxyHttpPort']
				, form.cleaned_data['proxySsl'], form.cleaned_data['proxySslPort']
				, form.cleaned_data['proxyFtp'], form.cleaned_data['proxyFtpPort']
				, form.cleaned_data['proxySocks'], form.cleaned_data['proxySocksPort'])

	else:
		form = ScanForm()
	
	form.fieldss['workers'].queryset = request.user.activeClient.workers.all()

	return render(request, "Visibility_Management/scan_create.html", {'assets': Asset.objects.all(), 'form': form})


def StartScan(name, worker, assets, proxy, proxyHttp="", proxyHttpPort="", proxySsl="", proxySslPort=""
	, proxyFtp="", proxyFtpPort="", proxySocks="", proxySocksPort=""  ):

	scan = Scan()
	scan.name = name

	name = "url" + str(scan.id) + ".txt"
	file = open(name, 'w')

	set_url = set()
	for a in assets: 
		set_url.add(a)
		print a
	for u in set_url: file.write(u + '\n')

	file.close()

	try:
		w2Task_id = SendFile(name)
	except:
		return "Error"

	if not proxy:
		scan.proxy = not proxy
		scan.proxyHttp = proxyHttp
		scan.proxyHttpPort = proxyHttpPort
		scan.proxySsl = proxySsl
		scan.proxySslPort = proxySslPort
		scan.proxyFtp = proxyFtp
		scan.proxyFtpPort = proxyFtpPort
		scan.proxySocks = proxySocks
		scan.proxySocksPort = proxySocksPort
		work = Core.worker_slave.start_screenshot.apply_async([not proxy, w2Task_id, 1, proxyHttp, proxyHttpPort, proxySsl, proxySslPort
	, proxyFtp, proxyFtpPort, proxySocks, proxySocksPort])

	else:
		scan.proxy = proxy
		work = Core.worker_slave.start_screenshot.apply_async([not proxy, w2Task_id])

	t = Task()
	t.task_id=work.task_id
	t.previus_id = w2Task_id
	t.total = len(set_url)*2
	t.task_type = "Visibility"
	t.save()

	worker.tasks.add(t)
	worker.save()

	scan.save()
	for a in assets:
		if "://" in a:
			a = a.split("://")[1]
		if ":" in a:
			a = a.split(":")[0]
		aux = Asset.objects.filter(address=a).exists()
		if not aux:
			aux = Asset()
			aux.address = a
			aux.save()
		else:
			aux = Asset.objects.get(address=a)
		scan.assets.add(aux)

	scan.task = t
	scan.save()

def SendFile(name):
	work2 = Core.worker_slave.rec_sock.apply_async()

	s = socket.socket()

	s.connect(("172.20.84.53",9999))

	f = open (name, "rb")
	l = f.read(1024)
	while (l):
	    s.send(l)
	    l = f.read(1024)
	s.close()

	while not work2.ready():
		time.sleep(1)

	f.close()
	s.close()

	os.system("rm " + name)

	return work2.task_id

def ScanFinish(request, task, url, title, port, status, image):
	task = base64.b64decode(task)
	url = base64.b64decode(url)
	title = base64.b64decode(title)
	port = base64.b64decode(port)
	status = base64.b64decode(status)
	image = base64.b64decode(image)

	
	finding = Finding()

	t = Task.objects.get(task_id=task)
	s = Scan.objects.get(task=t)
	u = url.split("://")[1].split(":")[0]
	a = Asset.objects.get(address=u)

	finding.scan = s
	finding.asset = a
	finding.url = url
	finding.title = title
	finding.port = port
	finding.status = status
	finding.image = image

	finding.save()
	
	return
	

def ScanDetail(request, pk):
	scan = Scan.objects.get(id=pk)
	return render(request, "Visibility_Management/scan_detail.html", {'scan' : scan} )
	

class ScanUpdate(UpdateView):
	model = Scan
	success_url = reverse_lazy('VIM_Scan_List')
	fields = ['assets']
	template_name = "Visibility_Management/scan.html"

class ScanDelete(DeleteView):
	model = Scan
	success_url = reverse_lazy('VIM_Scan_List')
	fields = ['assets']
	template_name = "Visibility_Management/scan_delete.html"

class AssetList(ListView):
	model = Asset
	template_name = "Visibility_Management/asset.html"

class FindingList(ListView):
	model = Finding
	template_name = "Visibility_Management/finding.html"

class AssetDetail(DetailView):
	model = Asset
	template_name = "Visibility_Management/asset_detail.html"

class FindingDetail(DetailView):
	model = Finding
	template_name = "Visibility_Management/finding_detail.html"

