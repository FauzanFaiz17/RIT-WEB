from django import forms
from .models import Aktivitas, Gambar
from users.models import Komunitas, Divisi

class AktivitasForm(forms.ModelForm):
    class Meta:
        model = Aktivitas
        fields = [
            'nama',
            'deskripsi',
            'tanggal_mulai',
            'tanggal_selesai',
            'komunitas',
            'divisi',
            'status',
            'jenis',
        ]
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),
            'tanggal_mulai': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tanggal_selesai': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'komunitas': forms.Select(attrs={'class': 'form-control'}),
            'divisi': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'jenis': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        jenis = kwargs.pop('jenis', None)
        super().__init__(*args, **kwargs)

        if jenis:
            self.fields['jenis'].initial = jenis
            self.fields['jenis'].disabled = True

        self.fields['komunitas'].queryset = Komunitas.objects.all()
        self.fields['divisi'].queryset = Divisi.objects.all()

        if user:
            jabatan = user.jabatan
            if jabatan == "Ketua":
                pass  # akses semua
            elif jabatan == "Ketua Komunitas":
                self.fields['komunitas'].queryset = Komunitas.objects.filter(kepala=user)
                self.fields['divisi'].queryset = Divisi.objects.none()
            elif jabatan == "Ketua Divisi":
                divisi_user = Divisi.objects.filter(kepala=user).first()
                if divisi_user:
                    self.fields['komunitas'].queryset = Komunitas.objects.filter(id=divisi_user.komunitas.id)
                    self.fields['divisi'].queryset = Divisi.objects.filter(kepala=user)
            else:
                self.fields['komunitas'].queryset = user.anggota_komunitas.all()
                self.fields['divisi'].queryset = user.kepala_divisi.all()


class GambarForm(forms.ModelForm):
    gambar = forms.ImageField(required=False)  # Tidak wajib diisi

    class Meta:
        model = Gambar
        fields = ['gambar']