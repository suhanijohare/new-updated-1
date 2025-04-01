from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Hospital, Ambulance, Patient

admin.site.register(Hospital)
admin.site.register(Ambulance)
admin.site.register(Patient)