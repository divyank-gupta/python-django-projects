from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse("It's index page of Blog app")
    return render(request,'blog/index.html')