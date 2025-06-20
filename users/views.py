from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, SignUpForm,UpdateProfileForm, UpdateFotoProfilForm

def index(request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'users/dashboard.html')

def maintenance(request):
    return render(request,'maintenance.html')

def game(request):
    return render(request,'guest/game_comunity.html')

def Anggota(request):
    return render(request,'users/anggota/index.html')


def surat(request):
    return render(request,'users/surat/index.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")  # ubah sesuai dashboard atau halaman utama
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'User created - please <a href="/login">login</a>.'
            success = True
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})





def contoh(request):
    return render(request,'users/profile.html')

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            print("form berhasil")
            form.save()
            # Tambahkan pesan sukses jika ingin
            return redirect('contoh')  # Ubah dengan nama URL-mu
        else:
             print("Form errors:", form.errors)
    else:
        form = UpdateProfileForm(instance=user)

    return render(request, 'users/profile.html', {'form': form})

@login_required
def update_foto_profil(request):
    if request.method == 'POST':
        form = UpdateFotoProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    return redirect('contoh')