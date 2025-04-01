from django.db import models
from django.contrib.auth.models import User

class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # other fields...


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_email = models.EmailField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    condition = models.TextField()
    admitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Ambulance(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.driver_name
