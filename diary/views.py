from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import Entry, EntryForm, Incident, IncidentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        entries = Entry.objects.filter(user=request.user)
        incidents = Incident.objects.filter(created_by=request.user)

        return render(request, 'diary/dashboard.html', {
            'entries': entries,
            'incidents': incidents
        })

# Entry
class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(CreateView):
    form_class = EntryForm
    model = Entry

    def get_initial(self):
        self.initial.update({ 'user': self.request.user })
        return self.initial

class EntryUpdateView(UpdateView):
    form_class = EntryForm
    model = Entry

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy('index')

# Incident
class IncidentDetailView(DetailView):
    model = Incident

class IncidentCreateView(CreateView):
    form_class = IncidentForm
    model = Incident

    def get_initial(self):
        self.initial.update({ 'created_by': self.request.user })
        return self.initial

class IncidentUpdateView(UpdateView):
    form_class = IncidentForm
    model = Incident

class IncidentDeleteView(DeleteView):
    model = Incident
    success_url = reverse_lazy('index')