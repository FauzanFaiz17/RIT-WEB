from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Keuangan, FotoKeuangan
from .forms import KeuanganForm
from .controller import hitung_sisa_keuangan
from django.db.models import Sum
from django.db import transaction
from django.core.paginator import Paginator


def keuangan(request):
    keuangan_queryset = Keuangan.objects.all().order_by('-tanggal')
    paginator = Paginator(keuangan_queryset, 5)  # tampilkan 5 data per halaman

    page_number = request.GET.get('page')  # ambil nomor halaman dari query string (?page=2)
    page_obj = paginator.get_page(page_number)  # ambil halaman terkait



    total_masuk = Keuangan.objects.filter(jenis='masuk').aggregate(Sum('jumlah'))['jumlah__sum'] or 0
    total_keluar = Keuangan.objects.filter(jenis='keluar').aggregate(Sum('jumlah'))['jumlah__sum'] or 0
    saldo = total_masuk - total_keluar
    context = {
        'keuangan_list': page_obj,
        'total_masuk': total_masuk,
        'total_keluar': total_keluar,
        'saldo': saldo
    }
    return render(request, 'users/keuangan/index.html', context)

def tambah_keuangan(request):
    if request.method == 'POST':
        form = KeuanganForm(request.POST)
        files = request.FILES.getlist('foto_keuangan')  # Ambil semua file di sini

        if form.is_valid():
            with transaction.atomic():
                keuangan = form.save()

                for file in files:
                    FotoKeuangan.objects.create(
                        keuangan=keuangan,
                        foto_keuangan=file
                    )

            hitung_sisa_keuangan()
            messages.success(request, "Data keuangan dan foto berhasil ditambahkan.")
            return redirect('keuangan')
        else:
            print("Form tidak valid:", form.errors)
    else:
        form = KeuanganForm()

    return render(request, 'users/keuangan/tambah.html', {
        'form': form,
    })


def edit_keuangan(request, pk):
    keuangan = get_object_or_404(Keuangan, pk=pk)

    if request.method == 'POST':
        form = KeuanganForm(request.POST, instance=keuangan)
        files = request.FILES.getlist('foto_keuangan')

        if form.is_valid():
            with transaction.atomic():
                form.save()
                for file in files:
                    FotoKeuangan.objects.create(
                        keuangan=keuangan,
                        foto_keuangan=file
                    )
            hitung_sisa_keuangan()
            messages.success(request, "Data keuangan berhasil diperbarui.")
            return redirect('keuangan')
        else:
            print("Form error:", form.errors)
    else:
        form = KeuanganForm(instance=keuangan)

    return render(request, 'users/keuangan/edit.html', {
        'form': form,
        'keuangan': keuangan,
    })


def hapus_keuangan(request, pk):
    keuangan = get_object_or_404(Keuangan, pk=pk)
    keuangan.delete()
    hitung_sisa_keuangan()
    messages.success(request, "Data keuangan berhasil dihapus.")
    return redirect('keuangan')

def hapus_foto_keuangan(request, foto_id):
    foto = get_object_or_404(FotoKeuangan, id=foto_id)
    if request.method == 'POST':
        foto.delete()
        messages.success(request, "Foto berhasil dihapus.")
    return redirect('edit_keuangan', pk=foto.keuangan.id)

def laporan_keuangan(request):
    keuangans = Keuangan.objects.order_by('tanggal', 'id')
    total_masuk = keuangans.filter(jenis='masuk').aggregate(Sum('jumlah'))['jumlah__sum'] or 0
    total_keluar = keuangans.filter(jenis='keluar').aggregate(Sum('jumlah'))['jumlah__sum'] or 0
    saldo = total_masuk - total_keluar
    return render(request, 'users/keuangan/laporan.html', {
        'keuangans': keuangans,
        'total_masuk': total_masuk,
        'total_keluar': total_keluar,
        'saldo': saldo
    })