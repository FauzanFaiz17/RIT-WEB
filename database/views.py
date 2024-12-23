from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("selamat datang di halaman database!")

# Create your views here.
