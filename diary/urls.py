from django.urls import path
from diary.views import DashboardView, CollectView

from . import views

urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    path('collect/', CollectView.as_view(), name='collect'),
]