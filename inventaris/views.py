from django.shortcuts import render, redirect, get_object_or_404
from .models import Barang, FotoBarang
from .forms import BarangForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.http import HttpResponseRedirect

def barang(request):
    barangs = Barang.objects.all().order_by('-tanggal')
    return render(request, 'users/inventaris/index.html', {'barangs': barangs})

def barang_create(request):
    if request.method == 'POST':
        form = BarangForm(request.POST)
        files = request.FILES.getlist('foto_barang')
        if form.is_valid():
            barang = form.save()
            for f in files:
                FotoBarang.objects.create(barang=barang, foto_barang=f)
            messages.success(request, "Data barang dan foto berhasil ditambahkan.")
            return redirect('barang')
    else:
        form = BarangForm()
    return render(request, 'users/inventaris/tambah.html', {'form': form})


def barang_update(request, pk):
    barang = get_object_or_404(Barang, pk=pk)
    if request.method == 'POST':
        form = BarangForm(request.POST, instance=barang)
        files = request.FILES.getlist('foto_barang')
        if form.is_valid():
            barang = form.save()
            for f in files:
                FotoBarang.objects.create(barang=barang, foto_barang=f)
            return redirect('barang')
    else:
        form = BarangForm(instance=barang)
    return render(request, 'users/inventaris/edit.html', {'form': form, 'barang':barang})

def barang_delete(request, pk):
    barang = get_object_or_404(Barang, pk=pk)
    barang.delete()
    messages.success(request, "barang berhasil dihapus.")
    return redirect('barang')

@require_POST
def hapus_foto_barang(request, pk):
    foto = get_object_or_404(FotoBarang, pk=pk)
    barang_id = foto.barang.id
    foto.delete()
    messages.success(request, "Foto berhasil dihapus.")
    return HttpResponseRedirect(reverse('barang_update', kwargs={'pk': barang_id}))