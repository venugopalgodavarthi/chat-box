from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request,'base.html')

@login_required(login_url='/login/')
def index(request):
    return render(request,'index.html')