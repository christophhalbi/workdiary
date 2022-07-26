from rest_framework import serializers
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('user', 'day', 'productivity_rating', 'happiness_rating', 'incidents')
