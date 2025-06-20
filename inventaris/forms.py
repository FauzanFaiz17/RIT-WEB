from django import forms
from .models import Barang

class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['nama_barang','sebelum','ditambah','digunakan','sisa','tanggal','keterangan']

