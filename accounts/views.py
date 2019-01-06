from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

'''
def user_login(request):
    
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(username=username, password=password)


       if user:
           if user.is_active:
               login(request, user)
               return HttpResponseRedirect('/')
           else:
               return HttpResponse("Your account is disabled.")

       else:
           return HttpResponse("not ok!.")

    else:
        return render(request, 'login.html')
'''
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def myself(request):
    return HttpResponse('myself!')