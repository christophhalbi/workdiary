from django.contrib import admin

from .models import Repo, Techstack, IncidentTag, Incident, Entry

admin.site.register(Repo)
admin.site.register(Techstack)
admin.site.register(IncidentTag)
admin.site.register(Incident)
admin.site.register(Entry)