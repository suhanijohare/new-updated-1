from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_hospital, name='register_hospital'),  # Register page as root
    path('home/', views.home, name='home'),
    path('dashboard/', views.hospital_dashboard, name='hospital_dashboard'),
]
