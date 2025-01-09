from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, KegiatanForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat, silahkan login')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")  # Debug Input

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"Login berhasil: {user.username}")  # Debug User Sukses
            login(request, user)
            return redirect('dashboard')
        else:
            # Debug Informasi Pengguna
            User = get_user_model()
            try:
                existing_user = User.objects.get(username=username)
                print("User ditemukan, tapi password salah.")  # Debug Password
            except User.DoesNotExist:
                print("User tidak ditemukan.")  # Debug Username

            messages.error(request, 'Username atau password salah.')
    return render(request, 'login.html')

def user_logout(request):
    return render(request, 'login.html')

def icons(request):
    return render(request, 'icons.html')

def map(request):
    return render(request, 'map.html')

def profile(request):
    return render(request, 'profile.html')

def tables(request):
    return render(request, 'tables.html')

def struktur(request):
    return render(request, 'struktur.html')

@login_required
def dashboard(request):
    if request.user.is_staff:
        return render(request, 'dashboard_admin.html')
    else:
        return render(request, 'dashboard_anggota.html')
    
@login_required
def buat_kegiatan(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = KegiatanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kegiatan berhasil dibuat')
            return redirect('dashboard')
    else:
        form = KegiatanForm()
    return render(request, 'buat_kegiatan.html', {'form': form})

@login_required
def edit_kegiatan(request, kegiatan_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    kegiatan = get_object_or_404(id=kegiatan_id)
    if request.method == 'POST':
        form = KegiatanForm(request.POST, instance=kegiatan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kegiatan berhasil diubah')
            return redirect('dashboard')
    else:
        form = KegiatanForm(instance=kegiatan)
    return render(request, 'edit_kegiatan.html', {'form': form})

@login_required
def hapus_kegiatan(request, kegiatan_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    
    kegiatan = get_object_or_404(id=kegiatan_id)
    if request.method == 'POST':
        kegiatan.delete()
        messages.success(request, 'Kegiatan berhasil dihapus')
        return redirect('dashboard')
    return render(request, 'hapus_kegiatan.html', {'kegiatan': kegiatan})



