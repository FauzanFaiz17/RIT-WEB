from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ProfilPengguna

class RegisterForm(UserCreationForm):
    class Meta:
        model = ProfilPengguna
        fields = ['username', 'email', 'nama_lengkap', 'no_hp', 'prodi', 'semester', 'npm', 'password1', 'password2']