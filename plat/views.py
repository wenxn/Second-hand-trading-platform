from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Plat

# Create your views here.
def plat_goods(request,pk):
    plat = get_object_or_404(Plat, pk=pk)
    return render(request, 'goods.html', {'plat': plat})


def add_goods(request,pk):
    plat = get_object_or_404(Plat, pk=pk)
    return render(request, 'add_goods.html', {'plat': plat})
    #return HttpResponse('111add_goods!')
'''
def add_goods(request):
    plats = Plat.objects.all()
    return render(request, 'add_goods.html', {'plats': plats})
'''

def delete_goods(request):
    return HttpResponse('delete_goods!')

def home(request):
    plats = Plat.objects.all()
    print(plats)
    return render(request, 'homepage.html', {'plats': plats})