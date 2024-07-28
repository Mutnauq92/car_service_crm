# crm/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "crm"

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/add/', views.car_create, name='car_create'),
    path('cars/<int:car_id>/quotations/', views.car_quotations, name='car_quotations'),
    path('quotations/', views.quotation_list, name='quotation_list'),
    path('quotations/add/', views.quotation_create, name='quotation_create'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.appointment_create, name='appointment_create'),
]

