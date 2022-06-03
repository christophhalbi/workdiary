from django.shortcuts import render
from django.views import View

class DashboardView(View):

    def get(self, request):
        return render(request, 'diary/dashboard.html')

class CollectView(View):

    def get(self, request):
        return render(request, 'diary/collect.html')