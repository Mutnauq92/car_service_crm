# crm/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Car, Quotation, Appointment, CustomerProfile
from .forms import CarForm, QuotationForm, AppointmentForm, UserRegistrationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            if not CustomerProfile.objects.filter(user=user).exists():
                CustomerProfile.objects.create(user=user)
            login(request, user)
            return redirect('crm:home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
    

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def car_list(request):
    if not hasattr(request.user, 'customerprofile') or not request.user.customerprofile.is_customer:
        return redirect('crm:home')
    cars = Car.objects.filter(owner=request.user)
    return render(request, 'car_list.html', {'cars': cars})


@login_required
def car_quotations(request, car_id):
    car = get_object_or_404(Car, id=car_id, owner=request.user)
    quotations = Quotation.objects.filter(car=car)
    total_parts_cost = sum(q.part_cost for q in quotations)
    total_labour_cost = sum(q.labour_cost for q in quotations)
    total_cost = total_parts_cost + total_labour_cost
    return render(request, 'crm/car_quotations.html', {
        'car': car,
        'quotations': quotations,
        'total_parts_cost': total_parts_cost,
        'total_labour_cost': total_labour_cost,
        'total_cost': total_cost
    })

@login_required
def car_create(request):
    if not hasattr(request.user, 'customerprofile') or not request.user.customerprofile.is_customer:
        return redirect('home')
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect(reverse('crm:car_list'))
    else:
        form = CarForm()
    return render(request, 'car_form.html', {'form': form})

@login_required
def quotation_list(request):
    quotations = Quotation.objects.filter(user=request.user)
    return render(request, 'quotation_list.html', {'quotations': quotations})


@login_required
def quotation_create(request):
    cars = Car.objects.filter(owner=request.user)
    if not cars:
        return redirect(reverse('crm:car_create'))  # Redirect if no cars are available
    
    if request.method == 'POST':
        form = QuotationForm(request.POST, user=request.user)
        if form.is_valid():
            quotation = form.save(commit=False)
            quotation.user = request.user
            quotation.save()
            return redirect(reverse('crm:quotation_list'))
    else:
        form = QuotationForm(user=request.user)
    return render(request, 'quotation_form.html', {'form': form})
    
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointment_list.html', {'appointments': appointments})

@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, user=request.user)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('crm:appointment_list')
    else:
        form = AppointmentForm(user=request.user)
    return render(request, 'appointment_form.html', {'form': form})
    
    
