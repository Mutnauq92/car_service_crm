# crm/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Car, Quotation, Appointment

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'reg', 'vin', 'color']

class QuotationForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=Car.objects.none(), required=True, empty_label="Select a vehicle")

    class Meta:
        model = Quotation
        fields = ['car', 'description', 'labor_cost', 'parts_cost']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(QuotationForm, self).__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(owner=user)


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['car', 'date', 'complaints']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),}

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['car'].queryset = Car.objects.filter(owner=user)