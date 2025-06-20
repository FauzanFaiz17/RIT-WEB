from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Aktivitas, Gambar
from .forms import AktivitasForm, GambarForm
from users.models import Komunitas, Divisi

from django.shortcuts import render, redirect
from .forms import AktivitasForm
from users.models import Komunitas, Divisi
from .models import Aktivitas, Gambar

def buat_kegiatan(request):
    komunitas_list = Komunitas.objects.all()
    divisi_list = Divisi.objects.all()

    if request.method == 'POST':
        form = AktivitasForm(request.POST, request.FILES)
        if form.is_valid():
            aktivitas = form.save(commit=False)

            # Set manual jenis
            aktivitas.jenis = "kegiatan"

            # Ambil dari dropdown manual
            komunitas_id = request.POST.get('komunitas')
            divisi_id = request.POST.get('divisi')

            if komunitas_id:
                aktivitas.komunitas_id = komunitas_id
            if divisi_id:
                aktivitas.divisi_id = divisi_id

            aktivitas.dibuat_oleh = request.user
            aktivitas.save()

            # Simpan gambar
            for gambar_file in request.FILES.getlist('gambar'):
                Gambar.objects.create(aktivitas=aktivitas, gambar=gambar_file)

            return redirect('daftar_kegiatan')
    else:
        form = AktivitasForm(initial={'jenis': 'kegiatan'})  # 👈 ini penting

    return render(request, 'aktivitas/buat_kegiatan.html', {
        'aktivitas_form': form,
        'komunitas_list': komunitas_list,
        'divisi_list': divisi_list,
    })

from django.shortcuts import get_object_or_404

def edit_kegiatan(request, pk):
    aktivitas = get_object_or_404(Aktivitas, pk=pk)
    komunitas_list = Komunitas.objects.all()
    divisi_list = Divisi.objects.all()

    if request.method == 'POST':
        form = AktivitasForm(request.POST, request.FILES, instance=aktivitas)
        if form.is_valid():
            aktivitas = form.save(commit=False)

            # Ambil komunitas dan divisi dari dropdown
            komunitas_id = request.POST.get('komunitas')
            divisi_id = request.POST.get('divisi')

            if komunitas_id:
                aktivitas.komunitas_id = komunitas_id
            if divisi_id:
                aktivitas.divisi_id = divisi_id

            aktivitas.jenis = 'kegiatan'  # tetap dipaksa jadi kegiatan
            aktivitas.save()

            # Simpan gambar tambahan kalau ada
            for gambar_file in request.FILES.getlist('gambar'):
                Gambar.objects.create(aktivitas=aktivitas, gambar=gambar_file)

            return redirect('daftar_kegiatan')  # atau halaman detail
    else:
        form = AktivitasForm(instance=aktivitas, initial={'jenis': 'kegiatan'})

    return render(request, 'aktivitas/edit_kegiatan.html', {
        'aktivitas_form': form,
        'komunitas_list': komunitas_list,
        'divisi_list': divisi_list,
        'aktivitas': aktivitas,
    })

def hapus_kegiatan(request, pk):
    aktivitas = get_object_or_404(Aktivitas, pk=pk)
    gambar_list = Gambar.objects.filter(aktivitas=aktivitas)

    if request.method == 'POST':
        # Hapus file dari storage
        for gambar in gambar_list:
            if gambar.gambar:
                gambar.gambar.delete(save=False)  # Ini yang hapus file fisiknya
        gambar_list.delete()
        aktivitas.delete()
        messages.success(request, "Kegiatan dan gambar berhasil dihapus.")
        return redirect('daftar_kegiatan')

    return render(request, 'aktivitas/konfirmasi_hapus.html', {
        'aktivitas': aktivitas,
    })

def buat_acara(request):
    komunitas_list = Komunitas.objects.all()
    divisi_list = Divisi.objects.all()

    if request.method == 'POST':
        form = AktivitasForm(request.POST, request.FILES)
        if form.is_valid():
            aktivitas = form.save(commit=False)

            # Set manual jenis
            aktivitas.jenis = "acara"

            # Ambil dari dropdown manual
            komunitas_id = request.POST.get('komunitas')
            divisi_id = request.POST.get('divisi')

            if komunitas_id:
                aktivitas.komunitas_id = komunitas_id
            if divisi_id:
                aktivitas.divisi_id = divisi_id

            aktivitas.dibuat_oleh = request.user
            aktivitas.save()

            # Simpan gambar
            for gambar_file in request.FILES.getlist('gambar'):
                Gambar.objects.create(aktivitas=aktivitas, gambar=gambar_file)

            return redirect('daftar_acara')
    else:
        form = AktivitasForm(initial={'jenis': 'acara'})  # 👈 ini penting

    return render(request, 'aktivitas/buat_acara.html', {
        'aktivitas_form': form,
        'komunitas_list': komunitas_list,
        'divisi_list': divisi_list,
    })

def edit_acara(request, pk):
    aktivitas = get_object_or_404(Aktivitas, pk=pk)
    komunitas_list = Komunitas.objects.all()
    divisi_list = Divisi.objects.all()

    if request.method == 'POST':
        form = AktivitasForm(request.POST, request.FILES, instance=aktivitas)
        if form.is_valid():
            aktivitas = form.save(commit=False)

            # Ambil komunitas dan divisi dari dropdown
            komunitas_id = request.POST.get('komunitas')
            divisi_id = request.POST.get('divisi')

            if komunitas_id:
                aktivitas.komunitas_id = komunitas_id
            if divisi_id:
                aktivitas.divisi_id = divisi_id

            aktivitas.jenis = 'acara'  # tetap dipaksa jadi kegiatan
            aktivitas.save()

            # Simpan gambar tambahan kalau ada
            for gambar_file in request.FILES.getlist('gambar'):
                Gambar.objects.create(aktivitas=aktivitas, gambar=gambar_file)

            return redirect('daftar_acara')  # atau halaman detail
    else:
        form = AktivitasForm(instance=aktivitas, initial={'jenis': 'acara'})

    return render(request, 'aktivitas/edit_acara.html', {
        'aktivitas_form': form,
        'komunitas_list': komunitas_list,
        'divisi_list': divisi_list,
        'aktivitas': aktivitas,
    })

def hapus_acara(request, pk):
    aktivitas = get_object_or_404(Aktivitas, pk=pk)
    gambar_list = Gambar.objects.filter(aktivitas=aktivitas)

    if request.method == 'POST':
        # Hapus file dari storage
        for gambar in gambar_list:
            if gambar.gambar:
                gambar.gambar.delete(save=False)  # Ini yang hapus file fisiknya
        gambar_list.delete()
        aktivitas.delete()
        messages.success(request, "Acara dan gambar berhasil dihapus.")
        return redirect('daftar_acara')

    return render(request, 'aktivitas/konfirmasi_hapus_copy.html', {
        'aktivitas': aktivitas,
    })

@login_required
def daftar_kegiatan(request):
    kegiatan_list = Aktivitas.objects.filter(jenis="kegiatan").order_by('-tanggal_mulai').prefetch_related('gambar_list')

    return render(request, 'aktivitas/daftar_kegiatan.html', {
        'kegiatan_list': kegiatan_list,
    })

@login_required
def daftar_acara(request):
    acara_list = Aktivitas.objects.filter(jenis="acara").order_by('-tanggal_mulai').prefetch_related('gambar_list')

    return render(request, 'aktivitas/daftar_acara.html', {
        'acara_list': acara_list,
    })
    