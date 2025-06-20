from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Keuangan
from .forms import KeuanganForm
from .controller import hitung_sisa_keuangan
from django.db.models import Sum

def keuangan(request):
    keuangan_list = Keuangan.objects.order_by('tanggal', 'id')
    total_masuk = Keuangan.objects.filter(jenis='masuk').aggregate(Sum('jumlah'))['jumlah__sum'] or 0
    total_keluar = Keuangan.objects.filter(jenis='keluar').aggregate(Sum('jumlah'))['jumlah__sum'] or 0
    saldo = total_masuk - total_keluar
    context = {
        'keuangan_list': keuangan_list,
        'total_masuk': total_masuk,
        'total_keluar': total_keluar,
        'saldo': saldo
    }
    return render(request, 'keuangan/index.html', context)

def tambah_keuangan(request):
    if request.method == 'POST':
        print("Form POST diterima")
        form = KeuanganForm(request.POST)
        if form.is_valid():
            print("Form valid")
            form.save()
            hitung_sisa_keuangan()
            messages.success(request, "Data keuangan berhasil ditambahkan.")
            return redirect('keuangan')
        else:
            print("Form tidak valid:", form.errors)
    else:
        form = KeuanganForm()
    return render(request, 'keuangan/tambah.html', {'form': form})


def edit_keuangan(request, pk):
    keuangan = get_object_or_404(Keuangan, pk=pk)
    if request.method == 'POST':
        form = KeuanganForm(request.POST, instance=keuangan)
        if form.is_valid():
            form.save()
            hitung_sisa_keuangan()
            messages.success(request, "Data keuangan berhasil diperbarui.")
            return redirect('keuangan')
    else:
        form = KeuanganForm(instance=keuangan)
    return render(request, 'keuangan/edit.html', {'form': form})


def hapus_keuangan(request, pk):
    keuangan = get_object_or_404(Keuangan, pk=pk)
    keuangan.delete()
    hitung_sisa_keuangan()
    messages.success(request, "Data keuangan berhasil dihapus.")
    return redirect('keuangan')

def laporan_keuangan(request):
    keuangans = Keuangan.objects.order_by('tanggal', 'id')
    total_masuk = keuangans.filter(jenis='masuk').aggregate(Sum('jumlah'))['jumlah__sum'] or 0
    total_keluar = keuangans.filter(jenis='keluar').aggregate(Sum('jumlah'))['jumlah__sum'] or 0
    saldo = total_masuk - total_keluar
    return render(request, 'keuangan/laporan.html', {
        'keuangans': keuangans,
        'total_masuk': total_masuk,
        'total_keluar': total_keluar,
        'saldo': saldo
    })