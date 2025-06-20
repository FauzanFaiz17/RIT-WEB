from django.shortcuts import render, redirect, get_object_or_404
from .forms import SuratForm
from .models import Surat
from django.contrib import messages

def surat(request):
    surats = Surat.objects.all().order_by('-tanggal')
    return render(request, 'users/surat/index.html', {'surats': surats})


def tambah_surat(request):
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('surat')  # ganti sesuai nama view daftar surat
    else:
        form = SuratForm()
    return render(request, 'users/surat/form_surat.html', {'form': form})

def edit_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES, instance=surat)
        if form.is_valid():
            form.save()
            return redirect('surat')
    else:
        form = SuratForm(instance=surat)
    return render(request, 'users/surat/form_surat.html', {'form': form})

def delete_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    surat.delete()
    messages.success(request, "surat berhasil dihapus.")
    return redirect('surat')