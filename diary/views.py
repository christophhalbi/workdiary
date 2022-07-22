from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from rest_framework import generics

from .models import Entry, EntryForm, Incident, IncidentForm
from .serializers import EntrySerializer

class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        entries = Entry.objects.filter(user=request.user).order_by('day')
        incidents = Incident.objects.filter(created_by=request.user).order_by('-created_at')

        return render(request, 'diary/dashboard.html', {
            'entries': entries,
            'incidents': incidents
        })

# Entry
class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(SuccessMessageMixin, CreateView):
    form_class = EntryForm
    model = Entry
    success_message = "Entry created!"

    def get_initial(self):
        self.initial.update({ 'user': self.request.user })
        return self.initial

class EntryUpdateView(SuccessMessageMixin, UpdateView):
    form_class = EntryForm
    model = Entry
    success_message = "Entry updated!"

class EntryDeleteView(SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('dashboard')
    success_message = "Entry deleted!"

class EntryListview(ListView):
    model = Entry

    def get_queryset(self):
        return Entry.objects.order_by('day')

class EntryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.order_by('day')

# Incident
class IncidentDetailView(DetailView):
    model = Incident

class IncidentCreateView(SuccessMessageMixin, CreateView):
    form_class = IncidentForm
    model = Incident
    success_message = "Incident created!"

    def get_initial(self):
        self.initial.update({ 'created_by': self.request.user })
        return self.initial

class IncidentUpdateView(SuccessMessageMixin, UpdateView):
    form_class = IncidentForm
    model = Incident
    success_message = "Incident updated!"

class IncidentDeleteView(SuccessMessageMixin, DeleteView):
    model = Incident
    success_url = reverse_lazy('dashboard')
    success_message = "Incident deleted!"

class IncidentListView(ListView):
    model = Incident

    def get_queryset(self):
        return Incident.objects.order_by('-created_at')