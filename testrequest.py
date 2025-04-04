import os
import django
import sys

# Debugging: Confirm script execution starts
print("Starting test script...")

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')  # Change if needed
django.setup()
print("Django setup complete.")

# Import necessary models
try:
    from rescueready.models import Patient, Ambulance, Driver, Paramedic  # djangochat models
    from hospital_server.models import Hospital  # hospital_server models
    print("Models imported successfully.")
except Exception as e:
    print("Error importing models:", e)

# Import requests to test APIs
import requests

# Define base URLs (change these if needed)
DJANGOCHAT_URL = "http://127.0.0.1:8000/"  # djangochat server
HOSPITAL_SERVER_URL = "http://127.0.0.1:8001/"  # hospital server

# Function to test database queries
def test_database():
    print("\nTesting database models...")
    try:
        print("Total Patients:", Patient.objects.count())
        print("Total Hospitals:", Hospital.objects.count())
    except Exception as e:
        print("Database error:", e)

# Function to test APIs
def test_apis():
    print("\nTesting APIs...")
    try:
        response = requests.get(DJANGOCHAT_URL + "api/patients/")
        print("Djangochat Patients API:", response.status_code, response.text)

        response = requests.get(HOSPITAL_SERVER_URL + "api/hospitals/")
        print("Hospital Server API:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("API request failed:", e)

if __name__ == "__main__":
    print("\nRunning database tests...")
    test_database()
    
    print("\nRunning API tests...")
    test_apis()
    
    print("\nTest script execution complete.")
