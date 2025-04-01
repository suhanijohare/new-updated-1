from django.db import models

# Patient model
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    disease = models.CharField(max_length=255)
    blood_pressure = models.CharField(max_length=50)  # e.g., "120/80"
    oxygen_level = models.IntegerField()
    gender = models.CharField(max_length=10)
    temperature = models.FloatField()  # in Celsius
    other_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Ambulance model
class Ambulance(models.Model):
    number_plate = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.number_plate

# Driver model
class Driver(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    license_number = models.CharField(max_length=50, unique=True)
    vehicle_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Paramedic model
class Paramedic(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15)
    license_number = models.CharField(max_length=50, unique=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    login_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
