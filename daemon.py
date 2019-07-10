# -*- coding: utf-8 -*-

import datetime, time, signal, sys, requests, json, smtplib, ssl
#import subprocess

MY_ADDRESS = 'talckar@gmail.com'
PASSWORD = '123fecci'
port = 465

msg = '''From: Talckar <talckar@gmail.com>
To: {}
Subject: {}
Estimado(a) {},

{}
Para mas detalles, ingrese al sistema Talckar: {}

Saludos,
Talckar'''

data1 = 'Le recordamos que tiene un viaje programado para el {} desde {} hasta {}.'
data2 = 'Le avisamos que su reserva programada para el {} desde {} hasta {} ha sido aceptada.'
data3 = 'Le avisamos que su reserva programada para el {} desde {} hasta {} ha sido rechazada.'
data4 = 'Le avisamos que hay una nueva solicitud de reserva programada para el {} desde {} hasta {}.'

def signal_handler(sig, frame):
	print('\nDaemmon desactivado')
	sys.exit(0)

def enviarMail(msg, dest):

	# Create a secure SSL context
	context = ssl.create_default_context()

	server= smtplib.SMTP_SSL("smtp.gmail.com", port)
	server.login(MY_ADDRESS, PASSWORD)
	server.sendmail("talckar@gmail.com", dest, msg)


if __name__ == "__main__":

	if len(sys.argv) != 3:
		print("Debe ingresar como argumento la ip y el puerto")
		sys.exit(0)

	server = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2])

	signal.signal(signal.SIGINT, signal_handler)
	print("Presiona Ctrl+C para cerrar el daemmon")
	while True:

		date = (datetime.datetime.now()).strftime("%Y-%m-%d")
		date2 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

		#Viajes

		url = server + "/apiViajes"
		headers = {"Content-Type" : "application/json"}

		resp = json.loads(requests.get(url, headers=headers).text)

		if len(resp) != 0:
			for r in resp:
				f = r['fecha'].split()[0].strip()

				if "-" not in f or len(f.split("-")) != 3:
					print("Formato incorrecto")
					continue

				if f == date or f == date2:

					r["origen"] = r["origen"].encode('utf8').replace("á", 'a').replace("é", 'e').replace("í", 'i').replace("ó", 'o').replace("ú", 'u').replace("ñ", 'n')
					r["destino"] = r["destino"].encode('utf8').replace("á", 'a').replace("é", 'e').replace("í", 'i').replace("ó", 'o').replace("ú", 'u').replace("ñ", 'n')

					data = data1.format(r["fecha"], r["origen"], r["destino"])
					msg1 = msg.format(r["correo"], "Notificacion Viaje Cercano", r["nombre"], data, server)

					try:
						enviarMail(msg1, r["correo"])
					except:
						print("Hubo un error en el envio del mail0")

					for u in r['users']:

						u["origen"] = u["origen"].encode('utf8').replace("á", 'a').replace("é", 'e').replace("í", 'i').replace("ó", 'o').replace("ú", 'u').replace("ñ", 'n')
						u["destino"] = u["destino"].encode('utf8').replace("á", 'a').replace("é", 'e').replace("í", 'i').replace("ó", 'o').replace("ú", 'u').replace("ñ", 'n')

						data = data1.format(u["fecha"], u["origen"], u["destino"])
						msg1 = msg.format(u["correo"], "Notificacion Viaje Cercano", u["nombre"], data, server)

						try:
							enviarMail(msg1, r["correo"])
						except:
							print("Hubo un error en el envio del mail1")
					
					url = server + "/apiNotificarViaje/" + str(r['id'])
					resp2 = requests.get(url, headers=headers).text
					print(resp2)


		#Reserva 1

		url = server + "/apiReservas"

		resp = json.loads(requests.get(url, headers=headers).text)
		if len(resp) != 0:
			for r in resp:

				if r['estado'] == 3:
					r["origen"] = r["origen"].encode('utf8').replace("á", 'a').replace("é", 'e').replace("í", 'i').replace("ó", 'o').replace("ú", 'u').replace("ñ", 'n')
					r["destino"] = r["destino"].encode('utf8').replace("á", 'a').replace("é", 'e').replace("í", 'i').replace("ó", 'o').replace("ú", 'u').replace("ñ", 'n')

					data = data2.format(r["fecha"], r["origen"], r["destino"])
					msg1 = msg.format(r["correo"], "Notificacion de Reserva Aceptada", r["nombre"], data, server)

					print(msg1)

					try:
						enviarMail(msg1, r["correo"])
					except:
						print("Hubo un error en el envio del mail2")

				elif r['estado'] == -2:
					r["origen"] = r["origen"].encode('utf8').replace("á", 'a').replace("é", 'e').replace("í", 'i').replace("ó", 'o').replace("ú", 'u').replace("ñ", 'n')
					r["destino"] = r["destino"].encode('utf8').replace("á", 'a').replace("é", 'e').replace("í", 'i').replace("ó", 'o').replace("ú", 'u').replace("ñ", 'n')

					data = data3.format(r["fecha"], r["origen"], r["destino"])
					msg1 = msg.format(r["correo"], "Notificacion de Reserva Rechazada", r["nombre"], data, server)

					print(msg1)

					try:
						enviarMail(msg1, r["correo"])
					except:
						print("Hubo un error en el envio del mail3")
						
				url = server + "/apiNotificarReserva/" + str(r['id'])
				resp2 = requests.get(url, headers=headers).text
				print(resp2)

		#Reserva 2

		url = server + "/apiReservasCond"

		resp = json.loads(requests.get(url, headers=headers).text)

		if len(resp) != 0:
			for r in resp:

				r["origen"] = r["origen"].encode('utf8').replace("á", 'a').replace("é", 'e').replace("í", 'i').replace("ó", 'o').replace("ú", 'u').replace("ñ", 'n')
				r["destino"] = r["destino"].encode('utf8').replace("á", 'a').replace("é", 'e').replace("í", 'i').replace("ó", 'o').replace("ú", 'u').replace("ñ", 'n')

				data = data4.format(r["fecha"], r["origen"], r["destino"])
				msg1 = msg.format(r["correo"], "Notificacion de nueva Solicitud", r["nombre"], data, server)

				print(msg1)

				try:
					enviarMail(msg1, r["correo"])
				except:
					print("Hubo un error en el envio del mail4")
						
				url = server + "/apiNotificarReserva/" + str(r['id'])
				resp2 = requests.get(url, headers=headers).text
				print(resp2)



		print(date)
		
		time.sleep(5)



'''
while True:
	time.sleep(5)
	print(datetime.datetime.now())
	#process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
		#output = process.communicate()[0]
		#print(output)
		 '''