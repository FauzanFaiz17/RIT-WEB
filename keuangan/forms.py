from django.forms import modelformset_factory
from django import forms
from .models import Keuangan, FotoKeuangan

class KeuanganForm(forms.ModelForm):
    class Meta:
        model = Keuangan
        fields = ['nama', 'jenis', 'tanggal', 'jumlah', 'keterangan']
        exclude = ['sisa']  # jangan tampilkan sisa

FotoKeuanganFormSet = modelformset_factory(
    FotoKeuangan,
    fields=('foto_keuangan',),
    extra=1,  # jumlah default form foto
    widgets={
        'foto_keuangan': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
)
