from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import Entry, EntryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        entries = Entry.objects.filter(user=request.user)

        return render(request, 'diary/dashboard.html', {'entries': entries})

class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(CreateView):
    form_class = EntryForm
    model = Entry

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EntryUpdateView(UpdateView):
    form_class = EntryForm
    model = Entry

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy('index')

