from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "form-control"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control"
        })
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "form-control"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Email",
            "class": "form-control"
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control"
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password check",
            "class": "form-control"
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    tanggal_lahir = forms.DateField(
        widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yyyy', 'class': 'form-control', 'type': 'text'}),
        required=False
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'tanggal_lahir', 'no_hp',
            'npm', 'prodi', 'semester', 'jabatan', 'foto_profil'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'no_hp': forms.TextInput(attrs={'class': 'form-control'}),
            'npm': forms.TextInput(attrs={'class': 'form-control'}),
            'prodi': forms.Select(attrs={'class': 'form-select'}),
            'semester': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 14}),
            'jabatan': forms.Select(attrs={'class': 'form-select'}),
        }

class UpdateFotoProfilForm(forms.ModelForm):
    foto_profil = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['foto_profil']
        widgets = {
            'foto_profil': forms.FileInput(attrs={'class': 'form-control'})
        }