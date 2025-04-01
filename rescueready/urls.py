from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register/', views.register_user, name='register_user'),  # Registration page
    path('checkview/', views.check_paramedic, name='check_paramedic'),  # Checkview for paramedics
    path('success/', views.success_page, name='success_page'),
    path('already-registered/', views.already_registered, name='already_registered'),
    path('api/patients/', views.get_patients, name='get_patients'),
    path('api/ambulances/', views.get_ambulances, name='get_ambulances'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

