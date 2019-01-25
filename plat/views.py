from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Plat,Good,Post
from .forms import goods_form,PostForm
from plat import models
from accounts.models import UserInfo
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def plat_goods(request):
    user = request.user
    user = UserInfo.objects.filter(username=user).first()
    goods = models.Good.objects.filter(starter=user).all()
    return render(request, 'goods.html',{'goods':goods})

@login_required
def add_goods(request):
    form = goods_form(request.POST)
    user = request.user
    user = UserInfo.objects.filter(username=user).first()
    if request.method == "POST":
        form = goods_form(request.POST)
        if form.is_valid():
            data = {
            'starter': user,
        }
            data.update(form.cleaned_data)
            v = Good.objects.create(**data)
            return redirect("/plat")
        else:
            print(form.errors)
    return render(request, 'add_bak.html', {'form':form})

@login_required
def edit_goods(request,id):
    obj = models.Good.objects.filter(id=id).first()
    form = goods_form(instance=obj)
    if request.method == "POST":
        form = goods_form(request.POST,instance=obj)
        if form.is_valid():
            v = models.Good.objects.filter(id=id).update(**form.cleaned_data)
            return redirect("/plat")
        else:
            print(form.errors)
    return render(request, 'edit_goods.html', {'form': form,'id':id})


@login_required
def del_goods(request,id):
    goods = models.Good.objects.filter(id=id)
    goods.delete()
    return redirect("/plat/")

def good_detail(request,id):
    goods = models.Good.objects.filter(id=id)
    good = models.Good.objects.filter(id=id).first()
    username = request.user
    userdetail = UserInfo.objects.filter(username=username).first()
    good.views +=1
    good.save()
    if request.method =='POST':
        message = request.POST['message']
        print(message)
        topic = models.Good.objects.filter(plat=good.plat).first()
        username = request.user
        userreal = UserInfo.objects.filter(username=username).first()
        post = Post.objects.create(
            message= 'message',
            update_by = userreal,
            topic=topic
        )
        return redirect("/plat/good_detail")
    return render(request, 'good_details.html', {'goods':goods,'userdetail':userdetail})


def home(request):
    plats = Plat.objects.all()
    return render(request, 'index.html', {'plats': plats})

def love_goods(request):
    return render(request, 'love_good.html')

def my_good(request):
    user = request.user
    user = UserInfo.objects.filter(username=user).first()
    goods = models.Good.objects.filter(starter=user).all()
    return render(request, 'my_good.html', {'goods': goods})