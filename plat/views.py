from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Plat,Good
from .forms import goods_form
from plat import models
from accounts.models import UserInfo


# Create your views here.
def plat_goods(request):
    #plat = models.Plat.objects.all(plat_name=plat_name)
    return render(request, 'goods.html')

def add_goods(request):
    form = goods_form()
    if request.method == "POST":
        print(request.POST)
        user_id = UserInfo.objects.filter(username='admin').first()
        print(user_id)
        data = {
            'starter': user_id,
        }
        form = goods_form(request.POST)

        if form.is_valid():
            data.update(form.cleaned_data)
            v = models.Good.objects.create(**data)
            return redirect("/plat/")
        else:
            print(form.errors)
    return render(request, 'add.html', {'form':form})

def edit_goods(request):
    form = goods_form()
    if request.method == "POST":
        form = goods_form(request.POST)
        if form.is_valid():
            v = models.Good.objects.filter().update(**form.cleaned_data)
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