from django.urls import path
from diary.views import DashboardView, EntryCreateView, EntryListCreateAPIView, EntryListview, EntryUpdateView, EntryDeleteView, EntryUnlinkIncidentView, EntryDetailView, IncidentCreateView, IncidentDeleteView, IncidentDetailView, IncidentListView, IncidentUpdateView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    # Entry
    path('entry-detail/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
    path('entry/add/', EntryCreateView.as_view(), name='entry-add'),
    path('entry/<int:pk>/', EntryUpdateView.as_view(), name='entry-update'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry-delete'),
    path('entry/<int:entry>/unlink-incident/<int:incident>', EntryUnlinkIncidentView.as_view(), name='entry-unlink-incident'),
    path('entrys/', EntryListview.as_view(), name='entry-list'),
    # Incident
    path('incident-detail/<int:pk>/', IncidentDetailView.as_view(), name='incident-detail'),
    path('incident/add/', IncidentCreateView.as_view(), name='incident-add'),
    path('incident/<int:pk>/', IncidentUpdateView.as_view(), name='incident-update'),
    path('incident/<int:pk>/delete/', IncidentDeleteView.as_view(), name='incident-delete'),
    path('incidents/', IncidentListView.as_view(), name='incident-list'),
    # API
    path('api/entry/', EntryListCreateAPIView.as_view() ),
]