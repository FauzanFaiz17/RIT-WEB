from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, KegiatanForm, GambarForm, ProfilForm, ProjectForm, TaskForm, SubtaskForm
from django.contrib import messages
from .models import Kegiatan, Gambar, ProfilPengguna, Komunitas, Project, Task, Subtask, Divisi
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .serializers import SubtaskSerializer
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

def projek_manage(request):
    komunitas_list = Komunitas.objects.all()
    divisi_list = Divisi.objects.all()
    projek_list = Project.objects.all()
    if request.method == 'POST':
        projek_form = ProjectForm(request.POST)
        if projek_form.is_valid():
            projek_form.save()
            return redirect('projek_manage')
    else:
        projek_form = ProjectForm()
    return render(request, 'projek_manage.html', {
        'komunitas_list': komunitas_list,
        'divisi_list': divisi_list,
        'projek_list': projek_list,
        'projek_form' : projek_form,
    })

@login_required
def hapus_projek(request, id): 
    projek = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        projek.delete()
        return redirect('projek_manage')
    return render(request, 'projek_manage.html', {'projek': projek})

@login_required
def projek_proses(request, id):
    projek = get_object_or_404(Project, id=id)
    projek_list = Project.objects.filter(id=id)
    task_list = Task.objects.filter(id_project=projek)
    subtask_list = Subtask.objects.filter(id_task__in=task_list)

    total_subtasks = subtask_list.count()
    completed_subtasks = subtask_list.filter(tanggal_selesai__isnull=False).count()

    progress_percentage = (completed_subtasks / total_subtasks * 100) if total_subtasks > 0 else 0

    # Hitung jumlah hari untuk setiap subtask sebelum dikirim ke template
    for subtask in subtask_list:
        if subtask.tanggal_mulai and subtask.tanggal_selesai:
            subtask.jumlah_hari = (subtask.tanggal_selesai - subtask.tanggal_mulai).days
        else:
            subtask.jumlah_hari = "-"
        subtask.save()

    if request.method == 'POST':
        if 'submit_task' in request.POST:  # Form Task
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                task = task_form.save(commit=False)
                task.id_project = projek  # Hubungkan task dengan project
                task.save()
                return redirect('projek_proses', id=id)
        else:
            task_form = TaskForm()

        if 'submit_subtask' in request.POST:
            subtask_form = SubtaskForm(request.POST)
            if subtask_form.is_valid():
                task_id = request.POST.get('task_id')
                task = get_object_or_404(Task, id=task_id)
                subtask = subtask_form.save(commit=False)
                subtask.id_task = task
                subtask.save()
                return redirect('projek_proses', id=id)
        else:
            subtask_form = SubtaskForm()

    else:
        task_form = TaskForm()
        subtask_form = SubtaskForm()

    return render(request, 'projek_proses.html', {
    'projek': projek,
    'projek_list': projek_list,
    'task_form': task_form,
    'subtask_form': subtask_form,
    'task_list': task_list,
    'subtask_list': subtask_list,
    "progress_percentage": round(progress_percentage, 2),
})

@login_required
def edit_subtask(request, id):
    subtask = get_object_or_404(Subtask, id=id)
    project_id = subtask.id_task.id_project.id
    
    if request.method == 'POST':
        subtask.nama = request.POST['nama']
        subtask.tanggal_mulai = request.POST['tanggal_mulai'] or None
        subtask.tanggal_selesai = request.POST['tanggal_selesai'] or None
        subtask.save()
        
        return redirect('projek_proses', id=project_id)

    return render(request, 'projek_proses.html', {'subtask': subtask})

@login_required
def edit_task(request, id):
    task_instance = get_object_or_404(Task, id=id)
    
    if request.method == 'POST':
        task_instance.nama = request.POST['nama']
        task_instance.tanggal_mulai = request.POST['tanggal_mulai'] or None
        task_instance.tanggal_selesai = request.POST['tanggal_selesai'] or None
        task_instance.save()  # Akan otomatis mengubah status sesuai logika di model
        return redirect('projek_proses', id=task_instance.id_project.id)

    return render(request, 'projek_proses.html', {'task': task_instance})

@api_view(['GET'])
def get_subtasks(request, project_id):
    """
    Mengambil semua subtask berdasarkan project_id (dari task yang ada di project)
    """
    subtasks = Subtask.objects.filter(id_task__id_project=project_id)
    serializer = SubtaskSerializer(subtasks, many=True)
    return Response(serializer.data)

@login_required
def profile(request):
    komunitas_list = Komunitas.objects.all()
    divisi_list = Divisi.objects.all()
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfilForm(instance=request.user)
    return render(request, 'profile.html', {
        'form': form,
        'komunitas_list': komunitas_list,
        'divisi_list': divisi_list,
    })

def struktur(request):
    return render(request, 'struktur.html')

def it_com(request):
    return render(request, 'it_com.html')

def gm_com(request):
    komunitas_gm = get_object_or_404(Komunitas, nama='Komunitas Game')
    users = ProfilPengguna.objects.filter(komunitas=komunitas_gm)
    return render(request, 'gm_com.html', {'users': users})

def web_dev(request):
    komunitas_it = get_object_or_404(Komunitas, nama='Komunitas IT')
    division = get_object_or_404(Divisi, nama='Divisi Web Development', komunitas=komunitas_it)
    users = ProfilPengguna.objects.filter(divisi=division)
    return render(request, 'web_dev.html', {'users': users})

def game_dev(request):
    komunitas_it = get_object_or_404(Komunitas, nama='Komunitas IT')
    division = get_object_or_404(Divisi, nama='Divisi Game Development', komunitas=komunitas_it)
    users = ProfilPengguna.objects.filter(divisi=division)
    return render(request, 'game_dev.html', {'users': users})

def iot_div(request):
    komunitas_it = get_object_or_404(Komunitas, nama='Komunitas IT')
    division = get_object_or_404(Divisi, nama='Divisi IoT', komunitas=komunitas_it)
    users = ProfilPengguna.objects.filter(divisi=division)
    return render(request, 'iot_div.html', {'users': users})

def keanggotaan(request):
    komunitas_it = get_object_or_404(Komunitas, nama='Komunitas IT')
    
    users = ProfilPengguna.objects.filter(
        komunitas=komunitas_it,
        divisi__isnull=True 
    )

    return render(request, 'keanggotaan.html', {'users': users})


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
    komunitas_list = Komunitas.objects.all()
    divisi_list = Divisi.objects.all()

    if request.method == 'POST':
        kegiatan_form = KegiatanForm(request.POST)
        if kegiatan_form.is_valid():
            kegiatan = kegiatan_form.save()  # Simpan kegiatan

            # Tangani upload banyak gambar
            for file in request.FILES.getlist('gambar'):
                Gambar.objects.create(kegiatan=kegiatan, gambar=file)

            return redirect('events')
        else:
            print("Kegiatan Form Errors:", kegiatan_form.errors)

    else:
        kegiatan_form = KegiatanForm()

    return render(request, 'tambah_kegiatan.html', {
        'kegiatan_form': kegiatan_form,
        'komunitas_list': komunitas_list,
        'divisi_list': divisi_list,
    })

@login_required
def edit_kegiatan(request, id):
    kegiatan = get_object_or_404(Kegiatan, id=id)

    # Ambil gambar pertama terkait kegiatan (jika ada), gunakan first() untuk mencegah error
    gambar_instance = kegiatan.gambar.first() if kegiatan.gambar.exists() else None

    kegiatan_form = KegiatanForm(request.POST or None, instance=kegiatan)
    gambar_form = GambarForm(request.POST or None, request.FILES or None, instance=gambar_instance)

    if request.method == 'POST':
        if kegiatan_form.is_valid() and gambar_form.is_valid():
            kegiatan_form.save()
            
            gambar = gambar_form.save(commit=False)
            gambar.kegiatan = kegiatan
            gambar.save()

            return redirect('events')

    return render(request, 'edit_kegiatan.html', {
        'kegiatan_form': kegiatan_form,
        'gambar_form': gambar_form,
        'kegiatan': kegiatan,
    })

@login_required
def hapus_kegiatan(request, id): 
    kegiatan = get_object_or_404(Kegiatan, id=id)
    if request.method == 'POST':
        kegiatan.delete()
        return redirect('events')
    return render(request, 'events.html', {'kegiatan': kegiatan})



