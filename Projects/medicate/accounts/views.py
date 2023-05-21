from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is home")

def about_us(request):
    return render(request, "about us.html")

def contact_us(request):
    return render(request, "contact us.html")


def donation(request):
    return render(request, "donation.html")


def medicate_registration(request):
    return render(request, "medicate registration.html")


def medicine(request):
    return render(request, "medicine.html")


def Sign_in(request):
    return render(request, "Sign-in.html")