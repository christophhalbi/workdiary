from django.urls import path
from diary.views import DashboardView, EntryCreateView, EntryUpdateView, EntryDeleteView, EntryDetailView

urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    path('entry-detail/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
    path('entry/add/', EntryCreateView.as_view(), name='entry-add'),
    path('entry/<int:pk>/', EntryUpdateView.as_view(), name='entry-update'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry-delete'),
]