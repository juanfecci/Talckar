# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *
from form import *

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import get_object_or_404

class AssetList(ListView):
	model = Asset
	template_name = "Asset_Management/asset_list.html"

class AssetDetail(DetailView):
	model = Asset
	template_name = "Asset_Management/asset_detail.html"

def AssetCreate(request):

	if request.method == 'POST':
		form = AssetForm(request.POST)
		if form.is_valid():

			text = form.cleaned_data['address'].split('\n')
			for i in text:

				aux = Asset.objects.filter(address=i).exists()
				if not aux:
					asset = Asset()
					asset.address = i
					asset.save()

			return render(request, 'Asset_Management/scan.html', {'form': form} )
	else: form = AssetForm()

	return render(request, 'Asset_Management/scan.html', {'form': form} )	