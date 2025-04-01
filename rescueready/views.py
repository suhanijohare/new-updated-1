from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from django.contrib.auth.models import User  # Use the Django User model for authentication
from rescueready.models import Patient, Driver, Paramedic, Ambulance  # Import your models
from rescueready.serializers import PatientSerializer, AmbulanceSerializer

# Home view - shows the main page or registration page
def home(request):
    return render(request, 'master.htm')  # Render the master.htm file

# View for handling paramedic login
def paramedic_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Get username from POST data
        try:
            username_details = User.objects.get(username=username)  # Query the User model
        except User.DoesNotExist:
            return render(request, 'error.html', {'message': 'User not found'})

        # Additional processing after user retrieval
        return render(request, 'success.html', {'username': username_details})

    return render(request, 'login.htm')  # Show login form if GET request

# View to check and register a paramedic
def check_paramedic(request):
    if request.method == 'POST':
        username = request.POST['paramedic-username']
        password = request.POST['paramedic-password']

        if Paramedic.objects.filter(name=username).exists():
            return redirect('/' + username + '/?password=' + password)  # Redirect if user exists
        else:
            # Create a new paramedic user if not found
            new_user = Paramedic(name=username)
            new_user.save()
            return redirect('/' + username + '/?password=' + password)

# User registration view
def register_user(request):
    if request.user.is_authenticated:  # If the user is logged in
        return redirect('already_registered')

    if request.method == 'POST':
        username = request.POST.get('username')
        hospital_id = request.POST.get('hospital_id')

        # Check if the user already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(hospital_id=hospital_id).exists():
            return redirect('already_registered')

        # Register new user
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hospital = request.POST.get('hospital')
        password = request.POST.get('password')

        new_user = User(
            username=username,
            password=password,  # Ensure to hash the password before saving
            # Add additional fields if required
        )
        new_user.set_password(password)  # Hash the password
        new_user.save()

        return redirect('success_page')  # Redirect to success page after registration

    return render(request, 'registration.htm')  # Render registration form for GET requests

# View for already registered users
def already_registered(request):
    return render(request, 'already_registered.html')  # Inform the user they are already registered

# Success page view after registration
def success_page(request):
    return render(request, 'success.html', {'message': 'Registration successful as driver!'})

# Serializer to handle patient data
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

# Serializer to handle ambulance data
class AmbulanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambulance
        fields = '__all__'

def dashboard(request):
    patients = Patient.objects.all()
    ambulances = Ambulance.objects.all()
    context = {'patients': patients, 'ambulances': ambulances}
    return render(request, 'rescueready/dashboard.html', context)

# API view to get patients
@api_view(['GET'])
def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

# API view to get ambulances
@api_view(['GET'])
def get_ambulances(request):
    ambulances = Ambulance.objects.all()
    serializer = AmbulanceSerializer(ambulances, many=True)
    return Response(serializer.data)
