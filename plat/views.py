from django.shortcuts import render
from django.http import HttpResponse
from .models import Plat

# Create your views here.
def plat_goods(request,pk):
    plat = Plat.objects.get(pk=pk)
    return render(request,'goods.html',{'plat':plat})

def delete_goods(request):
    return HttpResponse('delete_goods!')

def home(request):
    plats = Plat.objects.all()
    print(plats)
    return render(request, 'homepage.html',{'plats': plats})