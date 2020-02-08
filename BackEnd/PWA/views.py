from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import TempRegisterForm
# Create your views here.

@login_required
def index(request):
    return HttpResponse('this is my home page ')


def temp_register(request):
    
    temp_register_form= TempRegisterForm()
    ctx={'form':temp_register_form}
    return render(request,'temp_register_page.html',ctx)

def temp_register_submit(request):
    temp_register_request=TempRegisterForm(request.POST)

    if temp_register_request.is_valid():
        new_person=temp_register_request.save()
    return HttpResponse('you register succsessfull')

    