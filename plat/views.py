from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Plat,Good,Post,love
from .forms import goods_form
from plat import models
from accounts.models import UserInfo
from django.contrib.auth.decorators import login_required
from utils.pagination import Pagination
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.
@login_required
def plat_goods(request):
    user = request.user
    user = UserInfo.objects.filter(username=user).first()
    count = models.Good.objects.filter(starter=user).count()
    p = request.GET.get('p')
    path_info = request.META.get('PATH_INFO')
    req = Pagination(p, count, per_page_count=3)
    page_str = req.page_str(path_info)
    goods = models.Good.objects.filter(starter=user).all()[req.start:req.end]
    return render(request, 'goods.html',{'goods':goods,"page_str": page_str})

@login_required
def add_goods(request):
    form = goods_form(request.POST,request.FILES)
    user = request.user
    user = UserInfo.objects.filter(username=user).first()
    if request.method == "POST":
        form = goods_form(request.POST,request.FILES)
        if form.is_valid():
            data = {
            'starter': user,
        }
            data.update(form.cleaned_data)
            img = request.FILES.get('good_photo')
            v = Good.objects.create(**data)
            return redirect("/plat/my_good")
        else:
            print(form.errors)
    return render(request, 'add_bak.html', {'form':form})

@login_required
def edit_goods(request,id):
    obj = models.Good.objects.filter(id=id).first()
    form = goods_form(instance=obj)
    if request.method == "POST":
        form = goods_form(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            img = request.FILES.get('good_photo')
            v = models.Good.objects.filter(id=id).update(**form.cleaned_data)
            return redirect("/plat/my_good")
        else:
            print(form.errors)
    return render(request, 'edit_goods.html', {'form': form,'id':id})


@login_required
def del_goods(request,id):
    goods = models.Good.objects.filter(id=id)
    goods.delete()
    return redirect("/plat/my_good")

@login_required
def good_detail(request,id):
    goods = models.Good.objects.filter(id=id)
    good = models.Good.objects.filter(id=id).first()
    post_list = models.Post.objects.filter(topic=good).all()
    username = good.starter
    user = UserInfo.objects.filter(username=username).first()
    user_goods = models.Good.objects.filter(starter=user)
    userdetail = UserInfo.objects.filter(username=username).first()
    love_user = request.user
    love_user = UserInfo.objects.filter(username=love_user).first()
    fav = models.love.objects.filter(user_id=love_user, good_id=good).first()
    good.views +=1
    good.save()

    if request.method =='POST':
        message = request.POST['message']
        good = models.Good.objects.filter(id=id).first()
        username = request.user
        userreal = UserInfo.objects.filter(username=username).first()
        post = Post()
        post.message = message
        post.updated_at = timezone.now()
        post.created_by = userreal
        post.topic = good
        post.save()
        return redirect("/plat/good_%s" % id)
    return render(request, 'good_details.html', {'goods':goods,'userdetail':userdetail,'post_list':post_list,'user_goods':user_goods,'thisgood':good,'fav':fav})


def home(request):
    plats = Plat.objects.all()
    good = models.Good.objects.filter()
    return render(request, 'index.html', {'plats': plats,'good':good})

def loved(request,id):
    good = models.Good.objects.filter(id=id).first()
    loved= love()
    username = request.user
    user = UserInfo.objects.filter(username=username).first()
    loved.user_id = user
    loved.good_id = good
    loved.save()
    return redirect("/plat/good_%s" % id)

def unloved(request,id):
    good = models.Good.objects.filter(id=id).first()
    username = request.user
    user = UserInfo.objects.filter(username=username).first()
    fav = models.love.objects.filter(user_id=user,good_id=good)
    fav.delete()
    return redirect("/plat/good_%s" % id)

def love_goods(request):
    username = request.user
    userdetail = UserInfo.objects.filter(username=username).first()
    goods = models.Good.objects.filter(starter=userdetail)
    good = []
    fav = models.love.objects.filter(user_id=userdetail)
    fav_self = models.love.objects.filter(user_id=userdetail).count()
    good_self = models.Good.objects.filter(starter=userdetail).count()
    if fav:
       good = fav
    return render(request, 'love_good.html', {'userdetail':userdetail,'goods': goods,'good':good,'fav_self':fav_self,'good_self':good_self})

def my_good(request):
    user = request.user
    user = UserInfo.objects.filter(username=user).first()
    username = request.user
    userdetail = UserInfo.objects.filter(username=username).first()
    fav_self = models.love.objects.filter(user_id=userdetail).count()
    count = models.Good.objects.filter(starter=user).count()
    p = request.GET.get('p')
    path_info = request.META.get('PATH_INFO')
    req = Pagination(p, count, per_page_count=3)
    page_str = req.page_str(path_info)
    goods = models.Good.objects.filter(starter=user).all()[req.start:req.end]
    good_self = models.Good.objects.filter(starter=userdetail).count()
    return render(request, 'my_good.html', {'userdetail':userdetail,'goods': goods,"page_str": page_str,'fav_self':fav_self,'good_self':good_self})

@login_required
def delete_post(request,id):
    post = models.Post.objects.filter(id=id).first()
    id = post.topic.id
    post.delete()
    return redirect("/plat/good_%s" % id)

def reply_post(request):
    # 二级回复
    pass