from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from.models import Product
import math

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + math.ceil((n/4) - (n//4))
    params = {'no_of_slides':nSlides, 'range':range(1,nSlides ), 'product': products}
    return render(request,'shop/index.html')
    # return HttpResponse('We are at home')

def about(request):
    return render(request,'shop/about.html')