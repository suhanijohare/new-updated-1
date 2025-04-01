from rest_framework import serializers
from .models import Patient, Ambulance  # Ensure these models exist in models.py

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'  # Adjust according to your model fields

class AmbulanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambulance
        fields = '__all__'  # Adjust according to your model fields
