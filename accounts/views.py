from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import user_form,user_detail_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import UserInfo
from plat.models import love,Good


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
def myself_edit(request):
    user = request.user
    user_detail = UserInfo.objects.filter(username=user).first()
    fav_self = love.objects.filter(user_id=user_detail).count()
    good_self = Good.objects.filter(starter=user_detail).count()
    form = user_detail_form(instance=user_detail)
    if request.method == "POST":
        user = request.user
        user_detail = UserInfo.objects.filter(username=user).first()
        form = user_detail_form(request.POST,request.FILES, instance=user_detail)
        if form.is_valid():
            user = request.user
            v = UserInfo.objects.filter(username=user).update(**form.cleaned_data)
            return redirect("/accounts/myself")
        else:
            print(form.errors)
    return render(request, 'myself_edit.html',{'form':form,'user':user,'user_detail':user_detail,'fav_self':fav_self,'good_self':good_self})


def myself(request):
    user = request.user
    userdetail = UserInfo.objects.filter(username=user).first()
    form = user_detail_form(instance=userdetail)
    fav_self = love.objects.filter(user_id=userdetail).count()
    good_self = Good.objects.filter(starter=userdetail).count()
    return render(request, 'myself.html', {'user': user,'form':form,'userdetail':userdetail,'fav_self':fav_self,'good_self':good_self})
