from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ProfilPengguna, Kegiatan, Gambar, Project, Task, Subtask

class RegisterForm(UserCreationForm):
    class Meta:
        model = ProfilPengguna
        fields = ['username', 'email', 'npm', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-pill'}),
            'npm': forms.PasswordInput(attrs={'class': 'form-control rounded-pill'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control rounded-pill'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control rounded-pill'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        # Tambahkan nilai default untuk field tambahan
        user.nama_lengkap = "Tidak Diisi"
        user.no_hp = "0000000000"
        user.prodi = "Tidak Diisi"
        user.semester = 1
        if commit:
            user.save()
        return user
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if ProfilPengguna.objects.filter(email=email).exists():
            raise forms.ValidationError("Email sudah terdaftar. Gunakan email lain.")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class KegiatanForm(forms.ModelForm):
    class Meta:
        model = Kegiatan
        fields = ['nama', 'divisi', 'komunitas', 'deskripsi', 'tanggal_mulai', 'tanggal_selesai', 'status', 'jenis']
        widgets = {
            'tanggal_mulai': forms.DateInput(attrs={'type': 'date'}),
            'tanggal_selesai': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GambarForm(forms.ModelForm):
    gambar = forms.ImageField(required=False)  # Tidak wajib diisi

    class Meta:
        model = Gambar
        fields = ['gambar']

class ProfilForm(forms.ModelForm):
    class Meta:
        model = ProfilPengguna
        fields = [
            'nama_lengkap', 'no_hp', 'prodi', 'semester', 
            'foto_profil', 'tanggal_lahir', 'jabatan', 'komunitas', 'divisi'
        ]
        widgets = {
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'nama', 'nama_kepala', 'divisi', 'deskripsi'
        ]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'nama', 'tanggal_mulai', 'tanggal_selesai'
        ]
        widgets = {
            'tanggal_mulai': forms.DateInput(attrs={'type': 'date'}),
            'tanggal_selesai': forms.DateInput(attrs={'type': 'date'}),
        }

class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = [
            'nama', 'tanggal_mulai', 'tanggal_selesai'
        ]
        widgets = {
            'tanggal_mulai': forms.DateInput(attrs={'type': 'date'}),
            'tanggal_selesai': forms.DateInput(attrs={'type': 'date'}),
        }