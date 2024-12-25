from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ProfilPengguna, Kegiatan

class RegisterForm(UserCreationForm):
    class Meta:
        model = ProfilPengguna
        fields = ['username', 'email', 'nama_lengkap', 'no_hp', 'prodi', 'semester', 'npm', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class KegiatanForm(forms.ModelForm):
    class Meta:
        model = Kegiatan
        fields = ['nama', 'divisi', 'komunitas', 'deskripsi', 'tanggal_mulai', 'tanggal_selesai', 'status', 'jenis']
        widgets = {
            'tanggal_mulai': forms.DateInput(attrs={'type': 'date'}),
            'tanggal_selesai': forms.DateInput(attrs={'type': 'date'})
        }