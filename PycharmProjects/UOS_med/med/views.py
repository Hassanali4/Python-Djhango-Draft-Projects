from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request,'index.html')


def form(request):
    return render(request,'form.html')


def card(request):
    return render(request,'donation.html')


def blog(request):
    return render(request,'blog.html')


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')
