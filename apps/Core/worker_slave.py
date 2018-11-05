#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pkill -9 -f 'celery'

from __future__ import absolute_import

from celery import Celery

from Core.worker_module import *
import Core.worker_master 
import ssl

global app_slave, path, blanckmd5, port_set

broker_use_ssl = {
	'keyfile': '../minerva/ssl/key.pem',
	'certfile': '../minerva/ssl/cert.pem',
	'cert_reqs': ssl.CERT_REQUIRED
}

path = "../media/Temp/Visibility/"

app_slave = Celery('tasks', backend='amqp', broker='amqp://user1:pass1@172.20.84.53/host1')

app_slave.conf['CELERY_TASK_SERIALIZER'] = 'json'
app_slave.conf['CELERY_RESULT_SERIALIZER'] = 'json'
app_slave.conf['CELERY_ACCEPT_CONTENT'] = ['json']

blanckmd5 = 0
port_set = set()

@app_slave.task(bind=True)
def handshake(self, task_id):
	print "Start handshake"
	global path
	path_task = path
	#path_task = path + task_id

	value = md5Checksum("temp.zip")
	Core.worker_master.updateTask.apply_async([task_id, value])

@app_slave.task(bind=True)
def finish(self, task_id):
	pass



@app_slave.task(bind=True)
def start_screenshot(self, proxy, rec_id="",turn=1, proxyHttp="", proxyHttpPort="", proxySsl="", proxySslPort=""
	, proxyFtp="", proxyFtpPort="", proxySocks="", proxySocksPort="" ):
	print "Start Screenshot"
	print proxy, proxyHttp, proxyHttpPort, proxySsl, proxySslPort, proxyFtp, proxyFtpPort, proxySocks, proxySocksPort

	scan_id = self.request.id
	global blanckmd5, port_set
	path2 = "../media/Temp/Visibility/"
	path = "../media/Temp/Visibility/"+scan_id+"/"

	self.update_state(state="WAITING", meta={'PROCESSING':'---'})
	if turn == 1: os.system("rm "+ path+ "*.png")
	os.system("mkdir " + path)
	os.system("mkdir " + path+"Screenshots/")
	url_list = list()
	archivo = open(path2 + "url"+ rec_id +".txt")

	for line in archivo:
		url_list.append(line.strip())
		puerto = line.strip().split(":")[-1]
		port_set.add(puerto)

	archivo.close()
	driver = webdriver.Firefox(firefox_profile=firefoxProfile(port_set, proxy, proxyHttp, proxyHttpPort, proxySsl, proxySslPort
	, proxyFtp, proxyFtpPort, proxySocks, proxySocksPort))
	driver.set_page_load_timeout(10)

	createBlank(driver, port_set, path)
	
	blanckmd5 = md5Checksum(path + "blanck-crop.png")

	total = len(url_list)
	ij = 1
	it = 1

	if turn==1:
		files = open(path + "temp.txt", "wb")
		files.close()

	for url in url_list :
		self.update_state(state="PROCESSING", meta={'PROCESSING':str(ij) + "/" + str(total)})
		if turn > ij:
			ij += 1
			continue
		time.sleep(1)
		files = open(path + "temp.txt", "ab")
		driver, data, save, name = get_url(url,driver, True, port_set, blanckmd5, path, proxy, proxyHttp, proxyHttpPort, proxySsl, proxySslPort
	, proxyFtp, proxyFtpPort, proxySocks, proxySocksPort)
		if save:
			write_iterable_csv(files, list(data), name)
			it += 1
		ij += 1
		files.close()	

	driver.close()

	zip_name = 'temp_' + scan_id
	directory_name = path

	# Create 'path\to\zip_file.zip'
	shutil.make_archive(zip_name, 'zip', directory_name)
	

@app_slave.task(bind=True)
def env_sock(self, scan_id):
	print "Starting Send"
	path = "../media/Temp/Visibility/"+scan_id+"/"
	print "Waiting"

	s = socket.socket()
	while True:
		try:
			s.bind(("172.20.84.53",9998))
			break
		except: time.sleep(1)
		print "Connecting"

	s.listen(5) 
	print "Conected"

	sc, address = s.accept()
	name = 'temp_' + scan_id + ".zip"
	val = md5Checksum(name)
	f = open(name,'rb') #open in binary
	sc.send(val.encode())
	l = f.read(1024)
	while (l):
	    sc.send(l)
	    l = f.read(1024)
	
	f.close()
	sc.close()
	s.close()

@app_slave.task(bind=True)
def rec_sock(self):
	print "Start Receving"
	path = "../media/Temp/Visibility/"
	scan_id = self.request.id
	print "Waiting"

	s = socket.socket()
	while True:
		try:
			s.bind(("172.20.84.53",9999))
			break
		except: time.sleep(1)
		print "Connecting"

	s.listen(5) 

	sc, address = s.accept()
	name = path + "url" + scan_id + ".txt"
	f = open(name,'wb') #open in binary
	l = sc.recv(1024)
	while (l):
		f.write(l) 
		l = sc.recv(1024)

	f.close()
	sc.close()
	s.close()