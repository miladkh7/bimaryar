
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('tempRegister',views.temp_register,name='temp_register'),
    path('tempRegisterSubmit',views.temp_register_submit,name='submit_temp_register'),
]
