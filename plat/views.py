from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Plat,Goods
from .forms import goods_form
from plat import models


# Create your views here.
def plat_goods(request):
    goods = models.Goods.objects.filter()
    return render(request, 'goods.html')

def add_goods(request):
    form = goods_form()
    if request.method == "POST":
        username = request.session['username']
        user_id = models.User.objects.filter(username=username).first()
        data = {
            'starter': user_id,
        }
        form = goods_form(request.POST)

        if form.is_valid():
            data.update(form.cleaned_data)
            v = models.Goods.objects.create(**data)
            return redirect("/goods/")
        else:
            print(form.errors)
    return render(request, 'add_goods.html', {'form':form})

def edit_goods(request):
    form = goods_form()
    if request.method == "POST":
        form = goods_form(request.POST)
        if form.is_valid():
            v = models.Goods.objects.filter().update(**form.cleaned_data)
            print("修改的行数：", v)
            return redirect("goods.html")
    return render(request, "edit_goods.html", {
        'form': form,
    })

def del_goods(request):
    plat = get_object_or_404(Plat, pk=pk)
    return render(request, 'del_goods.html', {'plat': plat})

def home(request):
    plats = Plat.objects.all()
    return render(request, 'homepage.html', {'plats': plats})