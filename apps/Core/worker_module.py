
import subprocess, unicodedata, shutil, hashlib, time,  unicodedata, socket, os, sys

import pyscreenshot as ImageGrab
from PIL import Image

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException

#Calculate the md5 of a file
def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

#Take a screenshot from the pc
def takeScreenshot(name):
	os.system("gnome-screenshot --file=" + name)

#
def firefoxProfile(port_set, proxy, proxyHttp, proxyHttpPort, proxySsl, proxySslPort
	, proxyFtp, proxyFtpPort, proxySocks, proxySocksPort):
	FFprofile = webdriver.FirefoxProfile()
	FFprofile.set_preference('network.security.ports.banned.override', ','.join(port_set))  
	FFprofile.set_preference('webdriver.load.strategy', 'unstable')

	if proxy:
		FFprofile.set_preference("network.proxy.type", 1)

		FFprofile.set_preference("network.proxy.http", proxyHttp)
		if proxyHttpPort != "" and proxyHttpPort != "0":
			FFprofile.set_preference("network.proxy.http_port", int(proxyHttpPort))

		FFprofile.set_preference("network.proxy.ssl", proxySsl)
		if proxySslPort != "" and proxySslPort != "0":
			FFprofile.set_preference("network.proxy.ssl_port", int(proxySslPort))

		FFprofile.set_preference("network.proxy.ftp", proxyFtp)
		if proxyFtpPort != "" and proxyFtpPort != "0":
			FFprofile.set_preference("network.proxy.ftp_port", int(proxyFtpPort))

		FFprofile.set_preference("network.proxy.socks", proxySocks)
		if proxySocksPort != "" and proxySocksPort != "0":
			FFprofile.set_preference("network.proxy.socks_port", int(proxySocksPort))

	FFprofile.set_preference("browser.helperApps.neverAsk.saveToDisk", "*")
	FFprofile.set_preference("pdfjs.disabled", "true")
	FFprofile.update_preferences() 

	return FFprofile

def createBlank(driver, port_set, path):

	driver.get("about:blank")
	try:driver.get("https://5.5.5.5")
	except: pass

	time.sleep(5)
	takeScreenshot(path + "blanck.png")

	img = Image.open(path + "blanck.png")
	(maxX, maxY) = img.size

	bbox = (0,55,maxX, maxY-30)
	slice_bit=img.crop(bbox)

	slice_bit.save(path + "blanck-crop.png")
	

#Take a screenshot to the url from the browser
def get_url(url,driver,verif, port_set, blanckmd5, path, proxy, proxyHttp, proxyHttpPort, proxySsl, proxySslPort
	, proxyFtp, proxyFtpPort, proxySocks, proxySocksPort):
	bytes0 = 'd41d8cd98f00b204e9800998ecf8427e'
	path = path + "Screenshots/"
	name2 = ""
	i = 0
	tries = 1
	print "Getting.." + url

	data, title, status, page, save, name = [], "", "OK", url, False, ""

	while i < tries:

		try:
			driver.get("about:blank")
			driver.get(url)

			try:
				s = set(driver.window_handles)

				alert = driver.switch_to_alert()
				alert.dismiss()

				driver.switch_to_window(s.pop())
				print "Alert presented!"
				status = "Alert"
				name2 = url.replace("/","_").replace(":","_") + ".png" 
				name = path + url.replace("/","_").replace(":","_") + ".png" 
				takeScreenshot(name)

			except:
				pass
			time.sleep(5)
			name2 = url.replace("/","_").replace(":","_") + ".png" 
			name = (path + url.replace("/","_").replace(":","_") + ".png")
			driver.save_screenshot(name)
			if  bytes0 != md5Checksum(name):
				img = Image.open(name)
				w, h = img.size
				img = img.resize((int(w * 0.2), int(h * 0.2)), Image.ANTIALIAS)
				img.save(name, format='PNG')
			title = driver.title
			page = driver.current_url
			save = True

			print "Done!"
			break
		except TimeoutException:
			name2 = url.replace("/","_").replace(":","_") + ".png" 
			name = path + url.replace("/","_").replace(":","_") + ".png" 
			takeScreenshot(name)
			img = Image.open(name)
			(maxX, maxY) = img.size

			bbox = (0,55,maxX, maxY-30)
			slice_bit=img.crop(bbox)

			slice_bit.save(path + "temp.png")
			if md5Checksum(path + "temp.png") == blanckmd5:
				save = False
			else:
				save = True
				title = driver.title
				page = driver.current_url
				status = "Time Out"

			print "Timed out...."
		except WebDriverException, e:
			print "RELOADING DRIVER"
			print e
			
			print "CERRANDO DRIVER"

			try:

				alert = driver.switch_to_alert()
				alert.dismiss()

				driver.switch_to_window(s.pop())
				print "Alert presented!"
				status = "Alert"
			except:
				pass

			driver.close()
			driver = webdriver.Firefox(firefox_profile=firefoxProfile(port_set, proxy, proxyHttp, proxyHttpPort, proxySsl, proxySslPort
	, proxyFtp, proxyFtpPort, proxySocks, proxySocksPort))
			driver.set_page_load_timeout(10)

			driver.get("about:blank")
			if "ESSL_ERROR_RX_RECORD_TOO_LONG" not in str(e) and status != "Alert":
				save = True
				title = driver.title
				page = driver.current_url
				status = str(e)

			print "RELOADED DRIVER"
		except:
			print "Error"
			print "Unexpected error", sys.exc_info()[0]
			driver.close()
			driver = webdriver.Firefox(firefox_profile=firefoxProfile(port_set, proxy, proxyHttp, proxyHttpPort, proxySsl, proxySslPort
	, proxyFtp, proxyFtpPort, proxySocks, proxySocksPort))
			driver.set_page_load_timeout(10)

			driver.get("about:blank")

		i += 1

	try:

		ip = url.split(":")[1].split("/")[-1]
	except:
		ip = url
	secure = "SI" if "https" in url else "NO"
	try:
		if ":" in url: 
			port = url.split(":")[-1]
			if port == "": port=" "
			ip = url.split(":")[1].split("/")[-1]
		else: 
			port = " "
			ip = " "
	except:
		ip = ""
		port = ""
	url = url
	page = page
	title = title
	status = status
	data = ip, secure, port, url, page, title, status, name2
	return driver, data, save, name

def write_iterable_csv(file, line, name):
	line = ',;,'.join(line).replace('\n', '') + '\n'
	line = unicode(line)
	line = unicodedata.normalize('NFKD', line).encode('ascii','ignore')
	file.write(line)
	return
