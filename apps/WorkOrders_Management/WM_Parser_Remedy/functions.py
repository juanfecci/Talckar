import requests
import pickle
import time
import js2py
from datetime import datetime

HOME_URL = "https://f1cge.onbmc.com/arsys/BackChannel/?param=1182%2FGetTableEntryList%2F7%2Fonbmc-s19%2FSHR%3AOverviewConsole25%2FOverview%20Homepage%20Content9%2F3014442007%2Fonbmc-s25%2FSHR%3AUnion_OverviewConsole0%2F1%2F03%2F2002%2F0%2F12%2F5%5C400068500%5C13%2F1%2F9%2F400068500983%2F1%2F977%2F%20(%27230000009%27%20%3D%20%22MAINCHANGE%22%20AND%20(%20%271000000427%27%20%3D%20%22SGP000000013314%22%20OR%20%271000000079%27%20%3D%20%22SGP000000013314%22%20OR%20%271000003259%27%20%3D%20%22SGP000000013314%22)%20AND%20((%271000003561%27%20%3E%3D%201%20AND%20%271000003561%27%20%3C%3D%209)))%20OR%20(%27230000009%27%20%3D%20%22MAINHELPDESK%22%20AND%20(%20%271000000079%27%20%3D%20%22SGP000000013314%22)%20AND%20((%271000003561%27%20%3E%3D%200%20AND%20%271000003561%27%20%3C%3D%203)))%20OR%20(%27230000009%27%20%3D%20%22MAINWORKORDER%22%20AND%20(%20%271000000427%27%20%3D%20%22SGP000000013314%22%20OR%20%271000000079%27%20%3D%20%22SGP000000013314%22)%20AND%20(%20%271000000427%27%20%3D%20%22SGP000000013314%22%20OR%20%271000000079%27%20%3D%20%22SGP000000013314%22)%20AND%20(%271000003561%27%20%3D%200%20OR%20%271000003561%27%20%3D%201%20OR%20%271000003561%27%20%3D%202%20OR%20%271000003561%27%20%3D%203%20OR%20%271000003561%27%20%3D%204))%20OR%20(%27230000009%27%20%3D%20%22MAINKNOWLEDGEDATABASE%22%20AND%20(%20%271000000079%27%20%3D%20%22SGP000000013314%22)%20AND%20((%271000003561%27%20%3E%3D%204%20AND%20%271000003561%27%20%3C%3D%204)))%20OR%20(%27230000009%27%20%3D%20%22MAINKNOWNERROR%22%20AND%20(%20%271000000079%27%20%3D%20%22SGP000000013314%22)%20AND%20((%271000003561%27%20%3E%3D%200%20AND%20%271000003561%27%20%3C%3D%202)))%20OR%20(%27230000009%27%20%3D%20%22MAINPROBLEM%22%20AND%20(%20%271000000079%27%20%3D%20%22SGP000000013314%22)%20AND%20((%271000003561%27%20%3E%3D%200%20AND%20%271000003561%27%20%3C%3D%205)))5%2F1%2F1%2F45%2F1%2F1%2F11%2F12%2F0%2F2%2F0%2F&sToken="


import os, inspect


def save_obj(obj, name ):

    with open(os.path.dirname(os.path.abspath(inspect.stack()[0][1]))   + '/obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(os.path.dirname(os.path.abspath(inspect.stack()[0][1]))   + '/obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def get_headers():
	sToken = None
	print "Getting data..."
	while sToken == None:
		sendCookies = {

			"P":"0",
			"onbmc_pool":"!!DJ7SGdS3ONgLE4YrDsqNesIw4oz8IjmpQ56BuFYOwkBmPit0v3d9/O4XHPA9wsVvFOL/s9qTc42Mfg==/29CIpch5S4NuOcf0NPoVVp2IBJg==",
			"f1_prod":"_71fa70c6-8320-4963-86ee-be9cab875252",
			"st":"900",
			"lt":"60",
			"onbmc-s":"1504194076000",
			"FC":"1",
			"GKW":"%7B14%3A%7Bn%3A%22LASTID%22%2Ct%3A6%2Cv%3Anull%7D%2C15%3A%7Bn%3A%22LASTCOUNT%22%2Ct%3A7%2Cv%3A4%7D%7D",
			"lr":"true",
			}

		userAgent = {
			"Host": "f1cge.onbmc.com",
			"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Accept-Language": "en-US,en;q=0.5",
			"Accept-Encoding": "gzip, deflate, br",
			"Referer": "https://f1cge.onbmc.com/arsys/forms/onbmc-s/SHR%3ALandingConsole/Default+Administrator+View/?cacheid=eb824294",
			"Content-Type" : "application/x-www-form-urlencoded",
			"Connection": "close",
			"Upgrade-Insecure-Requests": "1",
			}

		data = {"timezone": "use_server", "tzind":"1"}

		url = "https://f1cge.onbmc.com/arsys/forms/onbmc-s/SHR%3ALandingConsole/Default+Administrator+View/?cacheid=eb824294"


		r = requests.post(url,headers=userAgent, cookies=sendCookies,data=data, allow_redirects=False)

		cookiesValidas = r.cookies
		print r.cookies
		cookiesValidas["f1_prod"] = "_71fa70c6-8320-4963-86ee-be9cab875252"

		if cookiesValidas.get("MJUID") != None:

			url = "https://f1cge.onbmc.com/arsys/forms/onbmc-s/SHR%3ALandingConsole/Default+Administrator+View/udd.js?ui=" + cookiesValidas.get("MJUID")

			r = requests.get(url,headers=userAgent, cookies=cookiesValidas)

			text = r.text

			text = text.split('sTok="')[-1].split('"')[0]
			sToken = text
		else:
			print "Error, retriying...."
			time.sleep(1)
			exit()
	print "Done!,"
	save_obj(cookiesValidas,"cookies")
	save_obj(userAgent,"headers")
	save_obj(sToken,"token")
	return userAgent, cookiesValidas, sToken


def authenticate():
	print "Cargando credenciales guardadas...."
	cookies = load_obj("cookies")
	headers = load_obj("headers")
	sToken = load_obj("token")

	

	r = requests.get(HOME_URL + sToken, headers=headers, cookies=cookies)
	if "Session is invalid or has timed out" in r.text:
		print "Credenciales expiradas, obteniendo nuevas..."
		cookies, headers, sToken = get_headers()
	print "Auntentificacion Satisfactoria!"
	return cookies,headers,sToken



def current_tickets(dHeaders):
	url = HOME_URL + dHeaders['sToken']
	r = requests.get(url,headers=dHeaders["headers"], cookies=dHeaders["cookies"])

	json_raw = r.text.split(";;")[0].split("his.result=")[-1]
	json_raw = "function a() {return " + json_raw + "} a()"


	
	py_obj = js2py.eval_js(json_raw)
	
	openTickets  = py_obj['r']

	cTickets = list()

	for x in py_obj['r']:
		d = 0

		id = x['i']
		resume = x['d'][3]["v"]
		created = x['d'][15]["v"]

		cTickets.append( (x['i'], x['d'][3]["v"]) )
		
	return cTickets

def get_details(wo,dHeaders):
	#THEY ARE CALLED NOTES HERE; BUT IT'S DETAILS
	TICKET_URL = "https://f1cge.onbmc.com/arsys/BackChannel/?param=219%2FGetTableEntryList%2F7%2Fonbmc-s13%2FHPD%3AHelp%20Desk18%2FBest%20Practice%20View9%2F3013896147%2Fonbmc-s11%2FHPD%3AWorkLog0%2F1%2F03%2F1009%2F2%2F1%2F42%2F-131%2F4%5C1%5C1%5C1000000161%5C99%5C1000000161%5C15%2F1%2F10%2F100000016120%2F1%2F15%2F---REPLACE_WO---5%2F1%2F1%2F45%2F1%2F1%2F01%2F02%2F0%2F2%2F0%2F&sToken="
	TICKET_URL = "https://f1cge.onbmc.com/arsys/BackChannel/?param=220%2FGetTableEntryList%2F7%2Fonbmc-s13%2FWOI%3AWorkOrder20%2FSimplified%20User%20View9%2F3013899237%2Fonbmc-s12%2FWOI%3AWorkInfo0%2F1%2F01%2F09%2F2%2F1%2F42%2F-131%2F4%5C1%5C1%5C1000002607%5C99%5C1000000182%5C15%2F1%2F10%2F100000018220%2F1%2F15%2F---REPLACE_WO---5%2F1%2F1%2F45%2F1%2F1%2F01%2F02%2F0%2F2%2F0%2F&sToken="
	url = TICKET_URL.replace('---REPLACE_WO---',wo) +  dHeaders['sToken']
	r = requests.get(url,headers=dHeaders["headers"], cookies=dHeaders["cookies"], allow_redirects=False)

	json_raw = r.text.split(";;")[0]

	#print json_raw
	py_obj = js2py.eval_js(json_raw)


	notes = []

	for note in py_obj['r']:
		id_note, note_data = note['i'], note['d']

		note_type = note_data[0]['v']
		note_title = note_data[1]['v']
		note_comments = note_data[2]['v']
		note_files = note_data[3]['v']
		note_date = note_data[4]['v']
		note_forwarder = note_data[9]['v']

		d_note = dict()

		d_note['id_note'] = id_note
		d_note['note_forwarder'] = note_forwarder
		d_note['note_type'] = note_type
		d_note['note_title'] = note_title
		d_note['note_comment'] = note_comments
		d_note['note_files'] = note_files
		d_note['date'] = note_date


#		print "id_note", id_note
#		print "note_forwarder", note_forwarder
#		print "note_type", note_type
#		print "note_title", note_title
#		print "note_comments", note_comments
#		print "note_files", note_files
#		print "note_date", note_date



		datetime_object = datetime.strptime(d_note['date'], '%d/%m/%Y %H:%M:%S')
		d_note['date'] = datetime_object


		notes.append(d_note)

	return notes


def get_log(wo, dHeaders):
	TICKET_URL = "https://f1cge.onbmc.com/arsys/BackChannel/?param=510%2FGetBulkTableEntryList%2F484%2F2%2F252%2F248%2FGetTableEntryList%2F7%2Fonbmc-s12%2FWOI%3AAuditLog18%2FDefault%20Admin%20View9%2F3017834007%2Fonbmc-s22%2FWOI%3AWorkOrder_AuditLog0%2F1%2F03%2F1002%2F0%2F37%2F1%5C4%5C1%5C1%5C450%5C99%5C301783800%5C5%5C301784100%5C24%2F2%2F9%2F3017841009%2F30178380025%2F2%2F3%2F1%3D115%2F---REPLACE_WO---5%2F2%2F1%2F41%2F48%2F2%2F1%2F11%2F01%2F12%2F0%2F2%2F0%2F222%2F218%2FGetTableEntryList%2F7%2Fonbmc-s12%2FWOI%3AAuditLog18%2FDefault%20Admin%20View9%2F3019510007%2Fonbmc-s16%2FNTE%3ANotifier%20Log0%2F1%2F01%2F09%2F2%2F1%2F02%2F-130%2F4%5C1%5C1%5C1000000205%5C99%5C300180400%5C13%2F1%2F9%2F30018040020%2F1%2F15%2F---REPLACE_WO---5%2F1%2F1%2F45%2F1%2F1%2F01%2F02%2F0%2F2%2F0%2F&sToken="
	url = TICKET_URL.replace('---REPLACE_WO---',wo) +  dHeaders['sToken']
	r = requests.get(url,headers=dHeaders["headers"], cookies=dHeaders["cookies"], allow_redirects=False)

	#print r.text

	json_raw = r.text.split(";this")[0].split("his.result=")[2]


	json_raw = "function a() {return " + json_raw[:-1] + "} a()"


	py_obj = js2py.eval_js(json_raw)

	logs = []

	for i in py_obj['r']:
		
		d_log = {
		"date" : i['d'][0]['v'],
		"user" : i['d'][5]['v'],
		"method" : i['d'][1]['v'],
		"event" : i['d'][2]['v'],
		"message" : i['d'][6]['p'],
}
		datetime_object = datetime.strptime(d_log['date'], '%d/%m/%Y %H:%M:%S')
		d_log['date'] = datetime_object
		logs.append( d_log )

	
	return logs
		


def get_ticket_data(wo,dHeaders):
	if "WO" in wo:
		TICKET_URL = "https://f1cge.onbmc.com/arsys/BackChannel/?param=603%2FGetQBETableEntryList%2F7%2Fonbmc-s13%2FWOI%3AWorkOrder20%2FSimplified%20User%20View4%2F10207%2Fonbmc-s13%2FWOI%3AWorkOrder0%2F1%2F01%2F09%2F2%2F1%2F02%2F-10%2F2%2F0%2F2%2F0%2F2%2F0%2F101%2F9%2F7%2F30009009%2F3012669009%2F3028313009%2F3030216009%2F3042563809%2F3777700209%2F4200501109%2F42005011110%2F1000000182200%2F9%2F2%2FWO2%2FWO7%2F0%20Never5%2F1%20Yes38%2F%3CBuscar%20usando%20ID%20de%20inicio%20de%20sesi%C3%B3n%3E38%2F%3CBuscar%20usando%20ID%20de%20inicio%20de%20sesi%C3%B3n%3E34%2FSRS%3AABYD%3ATask_Field_Template_Clone34%2FSRS%3AABYD%3ATask_Field_Template_Clone15%2F---REPLACE_WO---29%2F9%2F1%2F41%2F41%2F61%2F61%2F41%2F41%2F41%2F41%2F40%2F9%2F3999943821%2F019%2FARRoot150522715902239%2FID%20de%20orden%20de%20trabajo%2B%3D---REPLACE_WO---15%2F1%2F10%2F100000018220%2F1%2F15%2F---REPLACE_WO---2%2F0%2F2%2F0%2F&sToken="
		url = TICKET_URL.replace('---REPLACE_WO---',wo) +  dHeaders['sToken']
	elif "INC" in wo:
		TICKET_URL = "https://f1cge.onbmc.com/arsys/BackChannel/?param=934%2FGetQBETableEntryList%2F7%2Fonbmc-s13%2FHPD%3AHelp%20Desk18%2FBest%20Practice%20View4%2F10207%2Fonbmc-s13%2FHPD%3AHelp%20Desk0%2F1%2F01%2F09%2F2%2F1%2F02%2F-10%2F2%2F0%2F2%2F0%2F2%2F0%2F294%2F25%2F7%2F30009007%2F30051309%2F3012669009%2F3013986009%2F3013989009%2F3013990009%2F3027964009%2F3030216009%2F3042531809%2F3042531909%2F3042929509%2F3043140209%2F4001414409%2F4200501109%2F42005011110%2F100000009010%2F100000016110%2F100000028710%2F100000039710%2F100000039810%2F100000067610%2F100000068710%2F100000068810%2F100000512410%2F1000005125293%2F25%2F3%2FINC7%2F2000%20No3%2FINC24%2F8000%20General%20Information4%2F1%20No9%2F0%20Interno9%2F1087776004%2F1%20S%C3%AD1%2F11%2F17%2F2000%20No30%2F%3CBuscar%20usando%20ID%20corporativa%3E9%2FBMC.ASSET25%2FTMS%3AABYD%3ATask%20Field%20Clone25%2FTMS%3AABYD%3ATask%20Field%20Clone30%2F%3CBuscar%20usando%20ID%20corporativa%3E15%2F---REPLACE_INC---3%2FYes1%2F01%2F33%2FYes5%2F180005%2F180005%2F180005%2F1800078%2F25%2F1%2F41%2F61%2F41%2F61%2F61%2F61%2F71%2F61%2F21%2F21%2F61%2F41%2F41%2F41%2F41%2F41%2F41%2F41%2F21%2F21%2F41%2F71%2F71%2F71%2F70%2F9%2F3999943821%2F019%2FARRoot150522715902237%2FID%20de%20la%20incidencia*%2B%3D---REPLACE_INC---15%2F1%2F10%2F100000016120%2F1%2F15%2F---REPLACE_INC---2%2F0%2F2%2F0%2F&sToken="
		url = TICKET_URL.replace('---REPLACE_INC---',wo) +  dHeaders['sToken']
	r = requests.get(url,headers=dHeaders["headers"], cookies=dHeaders["cookies"], allow_redirects=False)
	json_raw = r.text.split(";;")[0].split("his.result=")[-1]
	json_raw = "function a() {return " + json_raw + "} a()"
	#print json_raw
	py_obj = js2py.eval_js(json_raw)


	t_status_wo =  	{ u'1': u'Pendiente',
		u'0': u'Asignado',
		u'3': u'Planificaci\xf3n',
		u'2': u'Esperando autorizaci\xf3n',
		u'5': u'Terminado',
		u'4': u'En curso',
		u'7': u'Cancelado',
		u'6': u'No Autorizado',
		u'8': u'Cerrado'
    }

	t_status_inc = { 0:"Nuevo",
    	    1:"Asignado",
	    2:"En curso",
	    3:"Pendiente",
	    4:"Resuelto",
	    5:"Cerrado",
	    6:"Cancelado"
    }

	id_petition = ""
	id_workOrder = wo

	client = ""
	client_id = ""
	resume = ""
	notes = ""

	user_asigned = ""
	group_asigned = ""

	status = ""
	status_cause = ""
	status_note = ""
	created = ""

	if "INC" in wo:
		for i in py_obj['e']:
			if u"i" in i:
				if i['i'] == 301572100:
					id_petition = i['v']
				elif i['i'] ==  1000000019:
					client1 = i['v']
				elif i['i'] ==  1000000018:
					client2 = i['v']
				elif i['i'] ==  1000000054:
					client_id = i['v']
				elif i['i'] == 1000000000:
					resume = i['v']
				elif i['i'] == 1000000151:
					notes = i['v']
				elif i['i'] == 1000003230:
					if 'v' in i:
						user_asigned = i['v']
				elif i['i'] == 1000000217:
					group_asigned = i['v']
				elif i['i'] == 1000005736:
					status = t_status_inc[int(i['v'])]
				elif i['i'] == 536870990:
					if 'v' in i:
						status_cause = i['v']
				elif i['i'] == 303408700:
					if 'v' in i:
						status_note = i['v']
				elif i['i'] == 1000003229:
					created = i['v']
		client = client1 + " " + client2
	elif "WO" in wo:
		for i in py_obj['e']:
			if u"i" in i:
				if i['i'] == 301572100:
					id_petition = i['v']
				elif i['i'] ==  301395400:
					client = i['v']
				elif i['i'] ==  1000000337:
					client_id = i['v']
				elif i['i'] == 1000000000:
					resume = i['v']
				elif i['i'] == 1000000151:
					if 'v' in i:
						notes = i['v']
				elif i['i'] == 1000003230:
					if 'v' in i:
						user_asigned = i['v']
				elif i['i'] == 1000003229:
					group_asigned = i['v']
				elif i['i'] == 301596600:
					status = t_status_wo[i['v']]
				elif i['i'] == 536870990:
					if 'v' in i:
						status_cause = i['v']
				elif i['i'] == 303408700:
					if 'v' in i:
						status_note = i['v']
				elif i['i'] == 1000003229:
					created = i['v']	


	bitacora = get_log(wo,dHeaders)	
	details = get_details(wo, dHeaders)

	ticket = {	"id_petition": id_petition,
				"id_workOrder": id_workOrder,
				"client": client,
				"client_id": client_id,
				"resume": resume,
				"notes": notes,
				"user_asigned": user_asigned,
				"group_asigned": group_asigned,
				"status": status,
				"status_cause": status_cause,
				"status_note": status_note,
				"created": created,
				"logs": bitacora,
				"details":details
			}
	return ticket
