from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hospital, Patient, Ambulance
import requests 
from rest_framework import serializers


def home(request):
    print("Home view called!")
    return render(request, 'home.html')

def register_hospital(request):
    print("Register Hospital view called!") 
    if request.method == "POST":
        # Process form data
        name = request.POST['name']
        address = request.POST['address']
        contact_email = request.POST['contact_email']

        hospital = Hospital.objects.create(name=name, address=address, contact_email=contact_email)
        
        # Redirect to home page after successful registration
        return redirect('home')

    return render(request, 'hospital/register_hospital.html')

def hospital_dashboard(request):
    # Fetch patient data from the main server
    response = requests.get('http://127.0.0.1:8000/api/patients/')
    patients = response.json()

    # Fetch ambulance data from the main server
    response_ambulances = requests.get('http://127.0.0.1:8000/api/ambulances/')
    ambulances = response_ambulances.json()

    context = {
        'patients': patients,
        'ambulances': ambulances,
    }
    return render(request, 'hospital/home.html', context)