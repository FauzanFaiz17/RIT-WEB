from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'nama_lengkap', 'no_hp',
            'tanggal_lahir', 'npm', 'prodi', 'semester',
            'jabatan', 'foto_profil', 'password1', 'password2'
        ]
        widgets = {
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date'}),
        }
