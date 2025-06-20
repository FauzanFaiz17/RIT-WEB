from django.db import models
from users.models import User, Divisi

class Project(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField(null=True, blank=True)
    kepala = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project_dipimpin')
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.nama


class Task(models.Model):
    STATUS_CHOICES = [
        ('belum_mulai', 'Belum Mulai'),
        ('sedang_berjalan', 'Sedang Berjalan'),
        ('selesai', 'Selesai'),
        ('tertunda', 'Tertunda'),
    ]

    nama = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='belum_mulai')

    def __str__(self):
        return f"{self.nama} ({self.project.nama})"


class Subtask(models.Model):
    STATUS_CHOICES = [
        ('belum_mulai', 'Belum Mulai'),
        ('sedang_berjalan', 'Sedang Berjalan'),
        ('selesai', 'Selesai'),
        ('tertunda', 'Tertunda'),
    ]

    nama = models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='subtasks')
    tanggal_mulai = models.DateField(null=True, blank=True)
    tanggal_selesai = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='belum_mulai')
    laporan_path = models.FileField(upload_to='laporan_subtask/', null=True, blank=True)

    def __str__(self):
        return f"{self.nama} - {self.assignee.namadepan if self.assignee else 'No Assignee'}"
