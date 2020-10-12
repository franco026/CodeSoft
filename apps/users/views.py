
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from apps.users.forms import UsersForms
from apps.users.models import Users
from django.contrib import messages

def account(request):
    return render(request,'account/account.html' )

def Login(request):
    if request.method == "POST":  
        password1 = request.POST['password']
        username1 = request.POST['username']
        try:  
            username2 = Users.objects.get(username=username1)
            password2 = Users.objects.get(password=password1)
           
            if username2 is not None and password2 is not None:
                return redirect('account')
            else:
                messages.info(request,'')
        except:  
            pass 
        
    return render(request, 'registration/login.html')



        
def CreateUser(request):  
    if request.method == "POST":  
        form = UsersForms(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('../')  
            except:  
                pass  
    else:  
        form = UsersForms()  
        return render(request,'registration/signup.html',{'form':form})  


