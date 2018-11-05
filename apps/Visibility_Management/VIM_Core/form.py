from django import forms
from django.forms import widgets
from models import *

class ScanForm(forms.Form):
	ports = forms.CharField(widget=forms.Textarea)
	assets = forms.CharField(widget=forms.Textarea, label = "Assets")
	proxy = forms.BooleanField(label = "Don't use proxy", required=False)
	proxyHttp = forms.CharField(label = "Proxy Http", required=False)
	proxyHttpPort = forms.CharField(label = "Proxy Http port", required=False)
	sameProxy = forms.BooleanField(label = "Use the same proxy and port", required=False)
	proxySsl = forms.CharField(label = "Proxy Ssl", required=False)
	proxySslPort = forms.CharField(label = "Proxy Ssl port", required=False)
	proxyFtp = forms.CharField(label = "Proxy Ftp", required=False)
	proxyFtpPort = forms.CharField(label = "Proxy Ftp port", required=False)
	proxySocks = forms.CharField(label = "Proxy Socks", required=False)
	proxySocksPort = forms.CharField(label = "Proxy Socks port", required=False)
	name = forms.CharField(label = "Name")
	workers = forms.ModelChoiceField(queryset=Worker.objects.none(), label = "Workers") 

   	
