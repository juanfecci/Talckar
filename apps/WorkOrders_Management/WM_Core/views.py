# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *
# Create your views here.

import datetime
import pytz


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import get_object_or_404


def dashboard(request):

	return render(request, 'WorkOrders_Management/dashboard.html',{})


def inbox(request):
	tickets = Inbox.objects.filter(active=True)
	for t in tickets:
		t.time_inbox = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - t.date_in
		t.time_inbox = t.time_inbox.total_seconds() / 60 / 60
		t.time_inbox = round(t.time_inbox,1)

	return render(request, 'WorkOrders_Management/inbox.html',{"tickets":tickets})


def following(request):
	tickets = Following.objects.filter(active=True)
	return render(request, 'WorkOrders_Management/following.html',{"tickets":tickets})

class FollowingList(ListView):
	model = Following
	template_name = "WorkOrders_Management/following_list.html"
	def get_queryset(self):
		queryset = Following.objects.all()
		for i in queryset:
				if i.ticket != None:
					if len(i.ticket.comentary_set.order_by("-date")) > 0:
						i.last_comment = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - i.ticket.comentary_set.order_by("-date")[0].date
						i.last_comment = str(round(i.last_comment.total_seconds() / (3600 * 24),1))
					else:
						i.last_comment = "9999999.9"
					

					if len(i.ticket.detail_set.order_by("-date")) > 0:
						i.last_note = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - i.ticket.detail_set.order_by("-date")[0].date
						i.last_note = str(round(i.last_note.total_seconds() / (3600 * 24),1))
					else:
						i.last_note = "9999999.9"

					if len(i.ticket.escalation_set.order_by("-date")) > 0:
						i.last_escalation = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - i.ticket.escalation_set.order_by("-date")[0].date
						i.last_escalation = str(round(i.last_escalation.total_seconds() / (3600 * 24),1))
					else:
						i.last_escalation = "9999999.9"

		return queryset


class FollowingDetail(DetailView):
	model = Following
	template_name = "WorkOrders_Management/following_detail.html"


class FollowingCreate(CreateView):
    model = Following
    success_url = reverse_lazy('following_list')
    fields = ['wo', "active", "service"]
    template_name = "WorkOrders_Management/following_form.html"


class FollowingUpdate(UpdateView):
    model = Following
    success_url = reverse_lazy('following_list')
    fields = ['wo', "active","service"]
    template_name = "WorkOrders_Management/following_form.html"


class FollowingDelete(DeleteView):
    model = Following
    success_url = reverse_lazy('following_list')
    template_name = "WorkOrders_Management/following_confirm_delete.html"


class TicketDetail(DetailView):
	model = Ticket
	template_name = "WorkOrders_Management/ticket_detail.html"


class ComentaryCreate(CreateView):
	model = Comentary
	template_name = "WorkOrders_Management/comentary_form.html"
	fields = ['comment']

	def get_success_url(self):
		return reverse_lazy('following_list')

	def form_valid(self, form):
		form.instance.ticket = get_object_or_404(Ticket,
                                                pk=self.kwargs['ticketPK'])
		form.instance.author = self.request.user
		return super(ComentaryCreate, self).form_valid(form)


class EscalationCreate(CreateView):
	model = Escalation
	template_name = "WorkOrders_Management/escalation_form.html"
	fields = ['method', 'recipient','comment']

	def get_success_url(self):
		#return reverse_lazy('ticket_detail',args=(self.object.ticket.id,))
		return reverse_lazy('following_list')

	def form_valid(self, form):
		form.instance.ticket = get_object_or_404(Ticket,
                                                pk=self.kwargs['ticketPK'])
		form.instance.author = self.request.user
		return super(EscalationCreate, self).form_valid(form)