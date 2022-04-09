from asyncio.windows_events import NULL
from this import d
from turtle import position
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from admin.models import Users
from django.contrib import messages 
from admin.forms import userforms
from django.contrib import messages
# # Create your views here.
def registermeter(request):
    if request.method == 'POST':
        cust = Users.objects.all()
            
        email = request.POST.get('email')
        citizenship = request.POST.get('citizenship')
        names = request.POST.get('name')
                  
        if cust.filter(email=email).exists() or cust.filter(citizenship=citizenship).exists():
            print('email taken')
            return redirect('registermeter')
        else:
            saverecord = Users(email=email,citizenship=citizenship,password="Pass",position="Meter Reader")
            saverecord.save()
            print('user created')
            return HttpResponse("Added in")
    else:
        return render(request,'admin.html')


def registercounter(request):
    if request.method == 'POST':
        cust = Users.objects.all()
            
        email = request.POST.get('email')
        citizenship = request.POST.get('citizenship')
        names = request.POST.get('name')
                  
        if cust.filter(email=email).exists() or cust.filter(citizenship=citizenship).exists():
            print('email taken')
            return redirect('registercounter')
        else:
            saverecord = Users(email=email,citizenship=citizenship,password="Pass",position="Counter")
            saverecord.save()
            print('user created')
            return HttpResponse("Added in")
    else:
        return render(request,'admin.html')

def displaycounter(request):
    showall=Users.objects.all()
    return render(request,'counter.html',{"data":showall})
    
def editcounter(request,email):
    editcounterobj=Users.objects.get(email=email)
    return render(request,'edit.html',{"Users":editcounterobj})

def updatecounter(request,email):
    updatecounter=Users.objects.get(email=email)   
    form=userforms(request.Post,instance=updatecounter)
    if form.is_valid():
        form.save()
        messages.success(request,'Record successfull')
        return render(request,'Editcounter.html',{"Users":updatecounter})

def counter():
     return None

def reader():
    return None

def customer():
    return None

def admain():
    return None

