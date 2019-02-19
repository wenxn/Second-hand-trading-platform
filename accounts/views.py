from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from .forms import user_form,user_detail_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import UserInfo
from plat.models import love,Good
from secondhand_platform import  settings


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
    user_detail = UserInfo.objects.get(username=user)
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

@login_required
def headimg(request):
    if request.method == 'POST':
        img = request.FILES.get('img_file')
        user = request.user
        user_detail = UserInfo.objects.get(username=user)
        if user_detail.photo:
            path = user_detail.photo.url.split('/')
            path[-1] = request.POST.get('img_name')
            path = path[-1]
            url = settings.MEDIA_ROOT + '/' + path
            with open(url, 'wb') as f:
                for chunk in img.chunks():
                    f.write(chunk)
            url = path
            user_detail.photo = url
            user_detail.save()
        else:
            path = request.POST.get('img_name')
            url = settings.MEDIA_ROOT + '/' + path
            with open(url, 'wb') as f:
                for chunk in img.chunks():
                    f.write(chunk)

            url = path
            user_detail.photo = url
            user_detail.save()

        return HttpResponse('图片上传成功')

@login_required
def myself(request):
    user = request.user
    userdetail = UserInfo.objects.filter(username=user).first()
    form = user_detail_form(instance=userdetail)
    fav_self = love.objects.filter(user_id=userdetail).count()
    good_self = Good.objects.filter(starter=userdetail).count()
    return render(request, 'myself.html', {'user': user,'form':form,'userdetail':userdetail,'fav_self':fav_self,'good_self':good_self})

def user_profile(request,id):
    user = request.user
    userdetail = UserInfo.objects.filter(nid=id).first()
    form = user_detail_form(instance=userdetail)
    fav_self = love.objects.filter(user_id=userdetail).count()
    good_self = Good.objects.filter(starter=userdetail).count()
    return render(request, 'user.html',{'user':user,'form':form,'userdetail':userdetail,'fav_self':fav_self,'good_self':good_self})