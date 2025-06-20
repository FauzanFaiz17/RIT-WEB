from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm, UpdateProfileForm, UpdateFotoProfilForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from projek_manajemen.models import Project, Task, Subtask
from kegiatan.models import Aktivitas
from django.utils import timezone
from datetime import timedelta

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
    member = User.objects.all()
    semua_projek = Project.objects.all()
    kegiatan = Aktivitas.objects.filter(jenis="kegiatan")
    kegiatan_baru = kegiatan.order_by('-tanggal_mulai')[:5] 
    projek_aktif = []

    for projek in semua_projek:
        tasks = Task.objects.filter(project=projek).prefetch_related('subtasks')

        total_subtasks = 0
        selesai_subtasks = 0

        for task in tasks:
            subtasks = task.subtasks.all()
            total_subtasks += subtasks.count()
            selesai_subtasks += subtasks.filter(status__iexact='selesai').count()

        if total_subtasks > 0:
            progress = int((selesai_subtasks / total_subtasks) * 100)
        else:
            progress = 0

        if total_subtasks > selesai_subtasks:
            projek_aktif.append({
                'projek': projek,
                'progress': progress
            })
    
    total_kegiatan = kegiatan.count()
    total_anggota = member.count()
    total_kegiatan_baru = kegiatan_baru.count()
    total_projek = Project.objects.count()

    tiga_bulan_lalu = timezone.now() - timedelta(days=90)
    projek_3_bulan_terakhir = Project.objects.filter(created_at__gte=tiga_bulan_lalu).count()

    return render(request, 'dashboard/dashboard.html', {
        'projek_aktif': projek_aktif,
        'total_projek': total_projek,
        'projek_3_bulan_terakhir': projek_3_bulan_terakhir,
        'total_anggota': total_anggota,
        'total_kegiatan': total_kegiatan,
        'total_kegiatan_baru': total_kegiatan_baru,
        'kegiatan': kegiatan_baru,
    })

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