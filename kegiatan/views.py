from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import KegiatanForm
from .models import FotoKegiatan, Kegiatan
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.http import HttpResponseRedirect

def kegiatan(request):
    kegiatan_list = Kegiatan.objects.filter(jenis="Kegiatan")
    return render(request,'users/kegiatan/index.html',  {'kegiatan_list': kegiatan_list})


def tambah_kegiatan(request):
    if request.method == 'POST':
        form = KegiatanForm(request.POST, request.FILES)
        if form.is_valid():
            kegiatan = form.save(commit=False)
            kegiatan.jenis = "Kegiatan"  # Set default jenis
            kegiatan.save()
            # Simpan foto kalau ada
            for f in request.FILES.getlist('foto_kegiatan'):
                FotoKegiatan.objects.create(kegiatan=kegiatan, foto_kegiatan=f)
            return redirect('kegiatan')  # atau sesuai url kamu
        else:
            print("Form errors:", form.errors)
    else:
        form = KegiatanForm()

    return render(request, 'users/kegiatan/tambah.html', {'form': form})

def edit_kegiatan(request, pk):
    kegiatan = get_object_or_404(Kegiatan, pk=pk)
    if request.method == 'POST':
        form = KegiatanForm(request.POST, request.FILES, instance=kegiatan)
        if form.is_valid():
            kegiatan = form.save()
            # Upload foto baru
            for uploaded_file in request.FILES.getlist('foto_kegiatan'):
                FotoKegiatan.objects.create(kegiatan=kegiatan, foto_kegiatan=uploaded_file)
            messages.success(request, "Kegiatan berhasil diperbarui.")
            return redirect('kegiatan')  # pastikan ini benar mengarah ke halaman daftar kegiatan
    else:
        form = KegiatanForm(instance=kegiatan)
    return render(request, 'users/kegiatan/edit.html', {'form': form, 'kegiatan': kegiatan})


def hapus_kegiatan(request, pk):
    kegiatan = get_object_or_404(Kegiatan, pk=pk)
    kegiatan.delete()
    messages.success(request, "Kegiatan berhasil dihapus.")
    return redirect('kegiatan')

@require_POST
def hapus_foto_kegiatan(request, pk):
    foto = get_object_or_404(FotoKegiatan, pk=pk)
    kegiatan_id = foto.kegiatan.id
    foto.delete()
    messages.success(request, "Foto berhasil dihapus.")
    return HttpResponseRedirect(reverse('edit_kegiatan', kwargs={'pk': kegiatan_id}))




# acara


def acara(request):
    acara_list = Kegiatan.objects.filter(jenis="Acara")
    return render(request,'users/acara/index.html',  {'acara_list': acara_list})


def tambah_acara(request):
    if request.method == 'POST':
        form = KegiatanForm(request.POST, request.FILES)
        if form.is_valid():
            kegiatan = form.save(commit=False)
            kegiatan.jenis = "Acara"  # Set default jenis
            kegiatan.save()
            # Simpan foto kalau ada
            for f in request.FILES.getlist('foto_kegiatan'):
                FotoKegiatan.objects.create(kegiatan=kegiatan, foto_kegiatan=f)
            return redirect('acara')  # atau sesuai url kamu
        else:
            print("Form errors:", form.errors)
    else:
        form = KegiatanForm()

    return render(request, 'users/acara/tambah.html', {'form': form})

def edit_acara(request, pk):
    kegiatan = get_object_or_404(Kegiatan, pk=pk)
    if request.method == 'POST':
        form = KegiatanForm(request.POST, request.FILES, instance=kegiatan)
        if form.is_valid():
            kegiatan = form.save()
            # Upload foto baru
            for uploaded_file in request.FILES.getlist('foto_kegiatan'):
                FotoKegiatan.objects.create(kegiatan=kegiatan, foto_kegiatan=uploaded_file)
            messages.success(request, "Acara berhasil diperbarui.")
            return redirect('acara')  # pastikan ini benar mengarah ke halaman daftar acara
    else:
        form = KegiatanForm(instance=kegiatan)
    return render(request, 'users/acara/edit.html', {'form': form, 'acara': acara})


def hapus_acara(request, pk):
    acara = get_object_or_404(Kegiatan, pk=pk)
    acara.delete()
    messages.success(request, "acara berhasil dihapus.")
    return redirect('acara')

@require_POST
def hapus_foto_acara(request, pk):
    foto = get_object_or_404(FotoKegiatan, pk=pk)
    acara_id = foto.acara.id
    foto.delete()
    messages.success(request, "Foto berhasil dihapus.")
    return HttpResponseRedirect(reverse('edit_acara', kwargs={'pk': acara_id}))