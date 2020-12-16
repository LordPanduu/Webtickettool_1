from typing import Dict, List

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ticket
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import request, HttpResponse


# Create your views here.
#def login(request):
  #  return render(request, 'dashboard/login.html')


def dashboard(request):
    context = {
        'tickets': Ticket.objects.all()
    }
    return render(request, 'Dashboard/dashboard.html', context)

class TicketListView(ListView):
    model = Ticket
    template_name = "Dashboard/dashboard.html"
    context_object_name = "tickets"
    #ordering = ["-date_posted"] Listet die Tickets das die neusten oben stehen

class TicketDetailView(DetailView):
        model = Ticket

class TicketCreateView(CreateView):
        model = Ticket
        fields =["title", "content", "author"]
     #def form_valid(self, form):
      #  from.instance.author = self.request.user
       # return super().from_valid(form)    automatische einfügen des Nutzers  (LoginRequiredMixin,UserPassesTestMixin, UpdateView)


class TicketUpdateView(UpdateView):
    model = Ticket
    fields = ["title", "content", "author"]
    # def form_valid(self, form):
    #  from.instance.author = self.request.user
    # return super().from_valid(form)    automatische einfügen des Nutzers  (LoginRequiredMixin,UserPassesTestMixin, UpdateView)

    # def test_func(self):
    # ticket = self.get_onject()
    # if self.reguest.user == ticket.author: #+ admin user noch hinzufügen
    #      return True
    #  return False

class TicketDeleteView(DeleteView):
        model = Ticket
        success_url = "/dashboard.html"
        # def test_func(self):
        # ticket = self.get_onject()
        # if self.reguest.user == ticket.author: #+ admin user noch hinzufügen
        #      return True
        #  return False