from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import user_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import UserInfo

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html',{'user':user})
        else:
            return render(request, 'login.html',{'form':form})
    if request.method == 'GET':
        form = user_form()
        return render(request, 'login.html',{'form':form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    form = user_form()
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            user_detail = UserInfo.objects.create(username=username, password=password)
            return redirect('/accounts/login')
    else:
        form = user_form()
    return render(request, 'signup.html',{'form':form})

@login_required
def myself(request):
    return render(request, 'myself.html',{})

