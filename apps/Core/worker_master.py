#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import Celery
import requests, json, time, socket, os, tempfile, hashlib

import Core.worker_slave
from zipfile import ZipFile
import base64, ssl
from Core.worker_module import *

broker_use_ssl = {
	'keyfile': '../minerva/ssl/key.pem',
	'certfile': '../minerva/ssl/cert.pem',
	'cert_reqs': ssl.CERT_REQUIRED
}

app = Celery('tasks', backend='amqp', broker='amqp://user1:pass1@localhost/host1')

app.conf.update(
	securyty_key = '../minerva/ssl/key.pem',
	securyty_certificate = '../minerva/ssl/cert.pem',
	securyty_cert_store = '../minerva/ssl/*.pem'
)

app.conf['CELERY_TASK_SERIALIZER'] = 'json'
app.conf['CELERY_RESULT_SERIALIZER'] = 'json'
app.conf['CELERY_ACCEPT_CONTENT'] = ['json']

'''
zip = ZipFile('file.zip')
zip.extractall()
'''


@app.task(bind=True)
def updateTask(self,t):
	directory = tempfile.mkdtemp() + "/"
	print "----------------------------------------"
	name = directory + "temp.zip"

	while True:

		worker1 = Core.worker_slave.env_sock.apply_async([t[0]]) 
		s = socket.socket()
		print time

		while True:
			try:
				s.connect(("172.20.84.53",9998))
				break
			except: time.sleep(1)
			print "Connecting"

		f = open (name, "wb")

		st_value = s.recv(32)
		
		l = s.recv(1024)
		while (l):
			f.write(l) 
			l = s.recv(1024)
		f.close()

		s.close()

		value = md5Checksum(name)
		print value
		print value.encode()
		print st_value
		if value.encode() == st_value:
			break

	print "yey"
	zip = ZipFile(name)
	zip.extractall(directory)
	f = open(directory + "temp.txt")
	dir2 = "../media/" + t[0]
	os.system("mkdir " + dir2)
	for line in f:
		line = line.strip().split(",;,")
		name2 = dir2 + "/" + line[7]
		os.system("cp "+ directory + "Screenshots/" + line[7] + " " + name2)
		image =base64.b64encode(name2) 
		task = base64.b64encode(t[0])
		url = base64.b64encode(line[3])
		title = base64.b64encode(line[5])
		port = base64.b64encode(line[2])
		status = base64.b64encode(line[6])
		print task, url, title, port, status, image
		requests.get("http://127.0.0.1:8000/Visibility_Management/scans/finish/"+task+"/"+url+"/"+title+"/"+port +"/"+ status + "/"+ image + "/")
	f.close()
	
	requests.get("http://127.0.0.1:8000/Task_Management/updateTask/" + '/'.join([t[0],"SUCCESS","-1"]))


@app.task(bind=True)		
def vigilant(self):

	while True:
		bruto = requests.get("http://127.0.0.1:8000/Task_Management/List")
		task1 = bruto.text

		tasks = json.loads(task1)
		print tasks

		for t in tasks:
			result = Core.worker_slave.app_slave.AsyncResult(t[0])

			print result.status
			print result.info
			
			if result.status == "PROCESSING":
				requests.get("http://127.0.0.1:8000/Task_Management/updateTask/" + '/'.join([t,"PROCESSING",result.info['PROCESSING'].split("/")[0]]))

			elif result.status == "SUCCESS":
				requests.get("http://127.0.0.1:8000/Task_Management/updateTask/" + '/'.join([t,"UPLOADING","-1"]))
				updateTask(t)
			else :
				requests.get("http://127.0.0.1:8000/Task_Management/updateTask/" + '/'.join([t,result.status,"-1"]))

		time.sleep(5)
