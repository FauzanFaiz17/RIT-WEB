from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, KegiatanForm, GambarForm
from django.contrib import messages
from .models import Kegiatan, Gambar
from django.forms import modelformset_factory
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
import os

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

def it_com(request):
    return render(request, 'it_com.html')

def web_dev(request):
    return render(request, 'web_dev.html')

@login_required
def dashboard(request):
    if request.user.is_staff:
        return render(request, 'dashboard_admin.html')
    else:
        return render(request, 'dashboard_anggota.html')

def events(request):
    kegiatan = Kegiatan.objects.prefetch_related('gambar').all()
    return render(request, 'events.html', {'kegiatan': kegiatan})

@login_required
def tambah_kegiatan(request):
    GambarFormSet = modelformset_factory(Gambar, form=GambarForm, extra=1)
    
    if request.method == 'POST':
        kegiatan_form = KegiatanForm(request.POST)
        gambar_formset = GambarFormSet(request.POST, request.FILES, queryset=Gambar.objects.none())
        
        if kegiatan_form.is_valid() and gambar_formset.is_valid():
            kegiatan = kegiatan_form.save()  # Simpan kegiatan
            for form in gambar_formset:
                if form.cleaned_data:  # Hanya simpan jika ada data
                    gambar = form.save(commit=False)
                    gambar.kegiatan = kegiatan  # Hubungkan gambar ke kegiatan
                    gambar.save()
            return redirect('events')
        else:
            # Debugging: tampilkan error form jika form tidak valid
            print("Kegiatan Form Errors:", kegiatan_form.errors)
            print("Gambar Formset Errors:", gambar_formset.errors)
    else:
        kegiatan_form = KegiatanForm()
        gambar_formset = GambarFormSet(queryset=Gambar.objects.none())

    return render(request, 'tambah_kegiatan.html', {
        'kegiatan_form': kegiatan_form,
        'gambar_formset': gambar_formset,
    })

@login_required
def edit_kegiatan(request, id):
    kegiatan = get_object_or_404(Kegiatan, id=id)
    GambarFormSet = modelformset_factory(Gambar, form=GambarForm, extra=1, can_delete=True)

    if request.method == 'POST':
        kegiatan_form = KegiatanForm(request.POST, instance=kegiatan)
        gambar_formset = GambarFormSet(request.POST, request.FILES, queryset=kegiatan.gambar.all())

        if kegiatan_form.is_valid() and gambar_formset.is_valid():
            kegiatan = kegiatan_form.save()

            for form in gambar_formset:
                if form.cleaned_data.get('DELETE') and form.instance.pk:
                    # Hapus file gambar dari media root
                    if form.instance.gambar and os.path.isfile(form.instance.gambar.path):
                        os.remove(form.instance.gambar.path)

                    # Hapus instance dari database
                    form.instance.delete()
                elif not form.cleaned_data.get('DELETE') and form.cleaned_data.get('gambar'):
                    gambar = form.save(commit=False)
                    gambar.kegiatan = kegiatan
                    gambar.save()

            return redirect('events')

    else:
        kegiatan_form = KegiatanForm(instance=kegiatan)
        gambar_formset = GambarFormSet(queryset=kegiatan.gambar.all())

    return render(request, 'edit_kegiatan.html', {
        'kegiatan_form': kegiatan_form,
        'gambar_formset': gambar_formset,
        'kegiatan': kegiatan,
    })

@login_required
def hapus_kegiatan(request, id): 
    kegiatan = get_object_or_404(Kegiatan, id=id)
    if request.method == 'POST':
        kegiatan.delete()
        return redirect('events')
    return render(request, 'hapus_kegiatan.html', {'kegiatan': kegiatan})



