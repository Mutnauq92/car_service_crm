from django.contrib import admin
from .models import CustomerProfile, Car

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_customer', 'address')
    search_fields = ('owner', 'make', 'model', 'reg', 'vin', 'color')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('owner', 'make', 'model', 'reg', 'vin', 'color')
    
