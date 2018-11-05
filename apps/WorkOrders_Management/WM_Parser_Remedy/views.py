# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from WorkOrders_Management.WM_Core.models import *

from functions import *

from django.core.mail import send_mail

CGE_EMAIL_RECEIVERS = [ "francisco.gallegos@cci-entel.cl", "patricio.albayay@cci-entel.cl", "muriel.lara@cci-entel.cl" ]

def get_dHeaders():
	while True:
		break
		try:
			cookies, headers, sToken = authenticate()
			dHeaders = { "cookies": cookies, "headers": headers, "sToken": sToken}
			break
		except:
			print "Problem getting inbox tickets, retrying....."

	cookies, headers, sToken = authenticate()
	dHeaders = { "cookies": cookies, "headers": headers, "sToken": sToken}
	return dHeaders

def send_mail_ticket(subject,message,receipts):
	send_mail(
	    subject,
	    message,
	    'francisco.gallegos@cci-entel.com',
	    receipts,
	    fail_silently=False,
	)
	return



def get_ticket(ticket):
	return get_ticket_data(ticket, dHeaders)


def ticket_change(ticket, last_date):
	subject = "[CGE][Seguimiento Tickets] Ticket: {0} a cambiado.".format(ticket.id_workOrder)
	

	message = '''
El ticket {0} ha cambiado, el detalle a continuacion:
-----------------------------------------------------
-----------------------------------------------------
Resumen: {1}
-----------------------------------------------------
Notas: {2}
-----------------------------------------------------
Usuario Asignado: {3}
-----------------------------------------------------
Grupo Asignado: {4}
-----------------------------------------------------
Estado: {5}
-----------------------------------------------------
-----------------------------------------------------
	'''.format(ticket.id_workOrder, ticket.resume, ticket.notes, ticket.user_asigned, ticket.group_asigned, ticket.status)
	for i in ticket.detail_set.filter(date__gt = last_date):
		message += '''
 
 -----------------------------------------------------
 EMISOR: {0}
 COMENTARIO: {1}
-----------------------------------------------------

		'''.format( i.forwarder, i.comment)
	message += '''
Atentamente,

███╗   ███╗ ██╗ ███╗   ██╗ ███████╗ ██████╗  ██╗   ██╗  █████╗ 
████╗ ████║ ██║ ████╗  ██║ ██╔════╝ ██╔══██╗ ██║   ██║ ██╔══██╗
██╔████╔██║ ██║ ██╔██╗ ██║ █████╗   ██████╔╝ ██║   ██║ ███████║
██║╚██╔╝██║ ██║ ██║╚██╗██║ ██╔══╝   ██╔══██╗ ╚██╗ ██╔╝ ██╔══██║
██║ ╚═╝ ██║ ██║ ██║ ╚████║ ███████╗ ██║  ██║  ╚████╔╝  ██║  ██║
╚═╝     ╚═╝ ╚═╝ ╚═╝  ╚═══╝ ╚══════╝ ╚═╝  ╚═╝   ╚═══╝   ╚═╝  ╚═╝
Management and Identification of Network Exposures, Reports and Vulnerabilities from Assements

------------------------------------------
  Working to have a better life everyday!
------------------------------------------
	'''

	send_mail_ticket(subject,message,CGE_EMAIL_RECEIVERS)

	print "MAIL SEND"

	return




# Create your views here.
def CRON():

	from django.core.mail import send_mail
	global dHeaders
	dHeaders = get_dHeaders()
	#get_tickets_inbox()
	get_tickets_following()



def update_ticket_info(ticket,):
		wo = ticket
		
		print "Processing... " + wo

		t = get_ticket_data(wo,dHeaders)

		oldT = Ticket.objects.filter(id_workOrder=t['id_workOrder'])

		if len(oldT) > 0:
			newTicket = oldT[0]
		else:
			newTicket = Ticket()

		newTicket.id_petition  = t['id_petition']
		newTicket.id_workOrder  = t['id_workOrder']

		newTicket.client  = t['client']
		newTicket.resume  = t['resume']
		newTicket.notes  = t['notes'][:500]

		newTicket.user_asigned  = t['user_asigned']
		newTicket.group_asigned  = t['group_asigned']

		newTicket.status  = t['status']
		newTicket.status_cause  = t['status_cause']
		newTicket.status_note  = t['status_note'][:500]
		#newTicket.created  = t['created']

		newTicket.save()

		print "Preocessing notes..."

		details = get_details(wo, dHeaders)
		n = False

		status = False

		for n in details[:1]:
			detail, status = Detail.objects.get_or_create(ticket = newTicket,
													id_detail = n['id_note'],
											type = n['note_type'],
											title = n['note_title'],
											comment = n['note_comment'],
											files = n['note_files'],
											date = n['date'],
											forwarder = n['note_forwarder']
													)
		print "Notes status:", status

		if status == True:
			print "Notes changes detected, writting logs..."




			#newTicket.detail_set.all().delete()

			for n in details:
				detail = Detail.objects.get_or_create(ticket = newTicket,
											id_detail = n['id_note'],
											type = n['note_type'],
											title = n['note_title'],
											comment = n['note_comment'],
											files = n['note_files'],
											date = n['date'],
											forwarder = n['note_forwarder']
											)
			#HERE WE SHOULD CHECK FOR CHANGES AND SEND MAIL ACORDINGLY
			if n:
				ticket_change(newTicket, n['date'])



		#CHECK IF CHANGES AND SAVEEEEEEE


		status = False
		
		print "Processing logs..."
		#Actualizamos los logs.
		for l in t['logs'][:1]:
			log,status = Log.objects.get_or_create(ticket = newTicket,
			date = l['date'],
			user = l['user'],
			method = l['method'],
			event = l['event'],
			message = l['message']
			)
			
		print "Log status:", status

		if status == True:
			print "Log changes detected, writting logs..."
			#newTicket.log_set.all().delete()

			for l in t['logs']:
				Log.objects.get_or_create(ticket = newTicket,
			date = l['date'],
			user = l['user'],
			method = l['method'],
			event = l['event'],
			message = l['message']
			)

		return newTicket


def get_tickets_following():
	print "TICKET ON FOLLOW:"


	tickets = Following.objects.filter(active=True)

	for t in tickets:
		if t.wo == "":
			t.wo = t.ticket.id_workOrder
			t.save()

	for t in tickets:
		
		wo = t.wo
		
		print "Processing... " + wo

		newTicket = update_ticket_info(wo)

		t.ticket = newTicket
		t.save()
		print "Done!"

	return

def update_end_date():
	inboxs = Inbox.objects.filter(active=True)
	for i in inboxs:
		i.active = False
		i.date_out = datetime.now()
		i.save()
	return


def update_inbox_ticket(ticket, date):
	inbox, status = Inbox.objects.get_or_create(ticket=ticket, active=True)
	if status == True:
		inbox.date_in = date
		inbox.save()
	return

def update_inbox_ticket_output(ticket, date):
	pass



def get_tickets_inbox():
	print "TICKETS ON INBOX"
#	while True:
#		#break
#
#		try:
#			cookies, headers, sToken = authenticate()
###			break
	#	except:
	##
	#cookies, headers, sToken = authenticate()
	#dHeaders = { "cookies": cookies, "headers": headers, "sToken": sToken}
	tickets = current_tickets(dHeaders)

	###########################################
	###########################################
	

	
	###########################################
	###########################################

	T = [ x for x,y in tickets]
	inboxs = Inbox.objects.filter(active=True)

	for i in inboxs:
		if i.ticket.id_workOrder not in T:
			
			i.active = False
			i.save()
			i = update_ticket_info(i.ticket.id_workOrder)
			USERS_CCI = ["FRANCISCO.GALLEGOS",
						"FRANCISCO.MUNOZ",
						"MARCELO.ARANEDA",
						"MDIAZL ",
						"RAPABLAZA",
						"SEGURIDADSST",
						"SEGURIDADEBC",
						"SEGURIDADOPERATIVAJA",
						"SEGURIDADPAQ",
						"SEGURIDADJP",
						"SEGURIDADGCG",
						"SEGURIDADFPC",
						"SEGURIDADDPM",
						"SEGURIDADAAM",
						"SEGURIDADCGP"]
			
			details = i.detail_set.filter(forwarder__in=USERS_CCI).order_by("-date")


			if len(details) > 0:
				i.date_out = details[0].date
			else:
				i.date_out = datetime.now()
			i.save()


	for t in tickets:
		wo,_ = t

		newTicket = update_ticket_info(wo)

		logsAsignated = newTicket.log_set.filter(message__contains="se ha asignado a su grupo 'CL-SOPORTE SEGURIDAD OPERATIVA'.")

		if len(logsAsignated) == 0:
			logsAsignated = newTicket.log_set.filter(message__contains="been assigned to your group 'CL-SOPORTE SEGURIDAD OPERATIVA'.")


		print "Processing inbox data..."
		update_inbox_ticket(newTicket, logsAsignated[0].date)



		print "Done!"

	return
