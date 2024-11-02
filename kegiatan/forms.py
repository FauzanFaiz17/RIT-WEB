from django import forms
from .models import Kegiatan, GambarKegiatan

class KegiatanForm(forms.ModelForm):
    class Meta:
        model = Kegiatan
        fields = ['nama', 'deskripsi', 'tanggal']

class GambarKegiatanForm(forms.ModelForm):
    class Meta:
        model = GambarKegiatan
        fields = ['gambar']
