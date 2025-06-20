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
    
    def save(self, commit=True):
        task = super().save(commit=False)

        # Hanya update status kalau task sudah punya ID
        if task.pk:
            subtasks = task.subtasks.all()
            if subtasks.exists() and all(sub.status == 'selesai' for sub in subtasks):
                task.status = 'selesai'
            else:
                task.status = 'sedang_berjalan'

        if commit:
            task.save(update_fields=['status'])

        return task 

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
    def __init__(self, *args, **kwargs):
        self.task = kwargs.pop('task', None)  # Terima task dari view
        super().__init__(*args, **kwargs)

    def clean_tanggal_selesai(self):
        tanggal_selesai = self.cleaned_data.get('tanggal_selesai')

        if self.task and tanggal_selesai:
            if tanggal_selesai > self.task.tanggal_selesai:
                raise forms.ValidationError(
                    f"Tanggal selesai subtask tidak boleh melebihi {self.task.tanggal_selesai}"
                )

        return tanggal_selesai
    
    def save(self, commit=True):
        instance = super().save(commit=False)

        # Jika tanggal_selesai diisi, otomatis ubah status menjadi "selesai"
        if instance.tanggal_selesai:
            instance.status = 'selesai'

        if commit:
            instance.save()

        return instance