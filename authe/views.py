from django.http import HttpResponse
from django.shortcuts import redirect, render
from authe.models import registermodel
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def register(request):
    if request.method=='POST' and request.FILES:
        print('hai')
        print(request.POST)
        print(request.FILES)
        p=request.POST['password']
        pa=request.POST['repassword']
        if p==pa:
            registermodel.objects.create(username=request.POST['username'],
                                     first_name=request.POST['firstname'],
                                     last_name=request.POST['lastname'],
                                     email=request.POST['email'],
                                     phone=request.POST['phone'],
                                     password=make_password(request.POST['password']),
                                     age=request.POST['age'],
                                     gender=request.POST['gender'],
                                     pic=request.FILES['pic'])
        return HttpResponse('data is stored')

    return render(request,'register.html')

def login1(request):
    if request.method=='POST':
        print(request.POST)
        user=request.POST['username']
        pas=request.POST['password']
        user1=authenticate(username=user,password=pas)
        if user1:
            print(user1)
            login(request,user1)
            return redirect('/i')
    return render(request,'login.html')

def logout1(request):
    logout(request)
    return redirect('/w')