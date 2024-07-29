# crm/models.py

from django.db import models
from django.contrib.auth.models import User

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

    @property
    def is_customer(self):
        return True
        

class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    reg = models.CharField(max_length=10)
    vin = models.CharField(max_length=17)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.make} {self.model} ({self.reg})"



class Quotation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # Temporarily allow null values
    description = models.TextField()
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    parts_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Quotation for {self.car} by {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateTimeField()
    complaints = models.TextField()

    def __str__(self):
        return f"Appointment for {self.car} on {self.date}"
        
        
        