from django.shortcuts import render, request

def show(request):
    return render(request, 'blog/nyoba.html')