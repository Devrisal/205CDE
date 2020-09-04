from django.shortcuts import render, redirect
from django.db import connections
# from django.contrib.auth
from django.http import HttpResponse
from .forms import RegisterForm
from .models import AddEvent
from .models import Usermodel 
from .forms import AddEventForm
from .forms import AddPackageForm
from .forms import AddPackage

from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    context ={}
    form =  RegisterForm(request.POST)
    if  form.is_valid():
        form.save()
    context['form'] = form
    return render(request,'register.html', context)

def edituser(request, id):  
    package = AddUser.objects.get(id=id)
    return render(request,'edituser.html',{'package':package})  

#add event
def addevent(request):

    allevents = AddEvent.objects.all()
    context = { 'allevents': allevents}
    form = AddEventForm(request.POST)
    if  form.is_valid():
        form.save()  
    context['form'] = form
    return render(request,'addevent.html', context) 

def editevent(request):  
    return render(request,'editevent.html')  

def updateevent(request, id):
    event = AddEvent.objects.get(id=id)  
    form = AddEvent(request.POST, instance = event)  
    if form.is_valid():  
        form.save()  
        return redirect("/addevent")  
    return render(request, 'editevent.html', {'event': event})
    
def delete(request, id):
   id = AddEvent.objects.get(id = id)
   if request.method == "POST":
        id.delete()
        return redirect('/gymsite/addevent')
   return render(request,'destroy.html')   
   
  

    

  #add pacakge
def addpackage(request):

    allpackages = AddPackage.objects.all()
    context = { 'allpackages': allpackages}
    form = AddPackageForm(request.POST)
    if  form.is_valid():
        form.save()  
    context['form'] = form
    return render(request,'addpackage.html', context)

def editpackage(request, id):  
    package = AddPackage.objects.get(id=id)
    return render(request,'editpackage.html',{'package':package})  


def updatepackage(request, id):
    package = AddPackage.objects.get(id=id)
    form = AddPackageForm(request.POST, instance = package)
    if  form.is_valid():
        form.save()
        return redirect('/gymsite/addpackage')  
   
    return render(request,'editpackage.html', {'package':package})
    
     

    
def deletepackage(request, id):
   id = AddPackage.objects.get(id = id)
   if request.method == "POST":
        id.delete()
        return redirect('/gymsite/addpackage')
     
   return render(request,'deletepackage.html')
    
def home(request):
    return render(request,'index.html') 

def login(request):
    return render(request,'login.html') 
def contact(request):
    return render(request,'contact.html') 

def dashboard(request):
    return render(request,'dashboard.html') 

def navbar(request):
    return render(request,'navbar.html')      


def viewuser(request):
    return render(request,'viewuser.html')    

def cousel(request):
    return render(request,'cousel.html')      

def advice(request):
    return render(request,'advice.html')  

def aboutus(request):
    return render(request,'aboutus.html')    

def viewpackages(request):
    return render(request,'viewpackages.html')   

def gallery(request):
    return render(request,'gallery.html')    

def fitnessclass(request):
    return render(request,'fitnessclass.html')                    


