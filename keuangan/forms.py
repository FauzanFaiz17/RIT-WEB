
from django import forms
from .models import Keuangan

class KeuanganForm(forms.ModelForm):
    class Meta:
        model = Keuangan
        fields = ['nama', 'jenis', 'tanggal', 'jumlah', 'keterangan']
        exclude = ['sisa']  # jangan tampilkan sisa

