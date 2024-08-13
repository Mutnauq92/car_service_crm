# car_service_crm/urls.py

from django.contrib import admin
from django.urls import path, include
from crm import views as crm_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', crm_views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('crm.urls')),
    #path('', crm_views.home, name='home'),
]

    

