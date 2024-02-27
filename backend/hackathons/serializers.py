from rest_framework import serializers
from .models import ScrapedHackathon

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedHackathon
        fields = '__all__'
