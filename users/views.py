from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm, UpdateProfileForm, UpdateFotoProfilForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def maintenance(request):
    return render(request,'maintenance.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Arahkan ke halaman login atau home
    else:
        form = SignUpForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Arahkan ke halaman dashboard atau home
            else:
                messages.error(request, "Username atau password salah.")
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil berhasil diperbarui.")
            return redirect('dashboard')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'auth/profile.html', {'form': form})

@login_required
def update_foto_profil(request):
    if request.method == 'POST':
        form = UpdateFotoProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    return redirect('profile')