from asyncio.windows_events import NULL
import email
from django.conf import ENVIRONMENT_VARIABLE
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Users,Customers

# Create your views here.
def login(request):
    # if request.method == 'POST':
    #     cust = Users.objects
        
    #     email=request.POST.get('email')
    #     passwords = request.POST.get('password')
    #     try:
    #         userdetail = cust.get(pk=email)
    #         if passwords = userdetail.password:
    #             return HttpResponse("Logged in")


            
    #     except:
            
    #            return HttpResponse("user name and password error")

        
    # else:
        
        return render(request,'login.html')



def register(request):
    if request.method == 'POST':
        cust = Customers.objects.all()
        middle_name=request.POST.get('middle_name')
        if (middle_name==NULL):
            name=  request.POST.get('first_name')+' '+ request.POST.get('last_name')
        else:
            name=  request.POST.get('first_name')+' '+middle_name+' '+ request.POST.get('last_name')    
        email = request.POST.get('email')
        citizenship = request.POST.get('citizenship')
        address = request.POST.get('district')+','+ request.POST.get('town')+','+ request.POST.get('municipality')+','+ request.POST.get('wardno')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1==password2:
            
            if cust.filter(email=email).exists() or cust.filter(citizenship=citizenship).exists():
                print('email taken')
                return redirect('register')
            else:
                saverecord = Customers(customername=name,email=email,citizenship=citizenship,address=address,password=password1)
                # saverecord.customername = name
                # saverecord.email = email
                # saverecord.citizenship = citizenship
                # saverecord.address= address
                # saverecord.password = password1
                saverecord.save()
                print('user created')
                return redirect('login')
        else:
        
            return HttpResponse("Wrong password or email")
    else:
        
        return render(request,'register.html')


    
    