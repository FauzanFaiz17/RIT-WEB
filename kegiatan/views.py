from django.shortcuts import render, redirect
from .models import Kegiatan, GambarKegiatan
from .forms import KegiatanForm, GambarKegiatanForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

def daftar_kegiatan(request):
    kegiatan = Kegiatan.objects.all()
    return render(request, 'daftar_kegiatan.html', {'kegiatan': kegiatan})

# @login_required
def tambah_kegiatan(request):
    if request.method == 'POST':
        kegiatan_form = KegiatanForm(request.POST)
        
        if kegiatan_form.is_valid():
            kegiatan = kegiatan_form.save()
            
            # Unggah beberapa gambar jika ada
            for gambar in request.FILES.getlist('gambar'):
                GambarKegiatan.objects.create(kegiatan=kegiatan, gambar=gambar)
            
            return redirect('daftar_kegiatan')
    else:
        kegiatan_form = KegiatanForm()
    
    return render(request, 'tambah_kegiatan.html', {
        'kegiatan_form': kegiatan_form,
    })