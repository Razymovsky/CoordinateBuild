from rest_framework import serializers
from .models import Organization, Entrance

class EntranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrance
        fields = ['id', 'organization', 'latitude', 'longitude']

class OrganizationSerializer(serializers.ModelSerializer):
    entrances = EntranceSerializer(many=True, read_only=True)  # Входы связаны с организацией

    class Meta:
        model = Organization
        fields = ['id', 'name', 'street', 'house_number', 'entrances']