from django.contrib import admin
from .models import PatientFile,PatientProfile,UserProfile,TempRegister
# Register your models here.
admin.site.register(PatientProfile)
admin.site.register(PatientFile)
admin.site.register(UserProfile)
admin.site.register(TempRegister)