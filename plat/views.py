from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_goods(request):
    return HttpResponse('add_goods')

def delete_goods(request):
    return HttpResponse('delete_goods!')

def home(request):

    return HttpResponse('Welcome!')