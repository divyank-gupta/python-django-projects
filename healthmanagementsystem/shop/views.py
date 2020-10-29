from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from.models import Product
import math

def index(request):
    # return HttpResponse("It's index page of Shop app")
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + math.ceil((n/4) - (n//4))
    params = {'no_of_slides':nSlides, 'range':range(1,nSlides ), 'product': products}
    return render(request,'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')

def search(request):
    return HttpResponse('We are at search')

def contact(request):
    return HttpResponse('We are at contact')

def tracker(request):
    return HttpResponse('We are at tracker')

def productView(request):
    return HttpResponse('We are at productView')

def checkout(request):
    return HttpResponse('We are at checkout')
