from django import forms
from .models import Keuangan

class KeuanganForm(forms.ModelForm):
    class Meta:
        model = Keuangan
        exclude = ['sisa']  # jangan tampilkan sisa