from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("aboutme",views.aboutme, name='aboutme'), 
    path("creation",views.creation, name='creation'), 
    path("custom",views.custom, name='custom'),
    path("signup",views.signup, name='signup'),
    path("Order",views.Order, name='Orderart')

    
]
