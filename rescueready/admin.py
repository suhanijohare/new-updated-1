from django.contrib import admin
from .models import Patient, Driver, Paramedic  # Import models correctly

# Register your models with the admin site
admin.site.register(Patient)
admin.site.register(Driver)
admin.site.register(Paramedic)



