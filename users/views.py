from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def index(request):
    return render(request,'index.html')

def maintenance(request):
    return render(request,'maintenance.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Arahkan ke halaman login atau home
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})
