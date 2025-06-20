from django import forms
from .models import Project, Task, Subtask

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['nama', 'deskripsi', 'kepala', 'divisi']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'kepala': forms.Select(attrs={'class': 'form-control'}),
            'divisi': forms.Select(attrs={'class': 'form-control'}),
        }

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['nama', 'tanggal_mulai', 'tanggal_selesai', 'status']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal_mulai': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tanggal_selesai': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=[('belum', 'Belum'), ('proses', 'Proses'), ('selesai', 'Selesai')])
        }

class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['nama', 'tanggal_mulai', 'tanggal_selesai', 'status']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal_mulai': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tanggal_selesai': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=[('belum', 'Belum'), ('proses', 'Proses'), ('selesai', 'Selesai')])
        }