from django import forms
from .models import Surat

class SuratForm(forms.ModelForm):
    class Meta:
        model = Surat
        fields = ['nomor', 'perihal', 'jenis', 'tanggal', 'keterangan', 'pengirim', 'file']
        widgets = {
            'tanggal': forms.DateInput(attrs={'type': 'date'}),
        }