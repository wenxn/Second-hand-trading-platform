from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from .forms import user_form
from django.contrib.auth.decorators import login_required

# Create your views here.

def user1_login(request):
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


def user_login(request):
    form = user_form()
    return render(request, 'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    form = user_form()
    if request.method == 'POST':
        print(request.POST)
        form = user_form(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = user_form()
    return render(request, 'signup.html',{'form':form})

def myself(request):
    return render(request, 'myself.html',{})

