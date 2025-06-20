from django.db import models
from users.models import Komunitas, Divisi, User

class Aktivitas(models.Model):
    STATUS_CHOICES = [
        ('terlaksana', 'Terlaksana'),
        ('sedang_terlaksana', 'Sedang Terlaksana'),
        ('tidak_terlaksana', 'Tidak Terlaksana'),
        ('belum_terlaksana', 'Belum Terlaksana'),
    ]

    JENIS_CHOICES = [
        ('kegiatan', 'Kegiatan'),
        ('acara', 'Acara'),
    ]

    nama = models.CharField(max_length=255)
    deskripsi = models.TextField(null=True, blank=True)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    komunitas = models.ForeignKey(Komunitas, on_delete=models.SET_NULL, null=True, blank=True)
    divisi = models.ForeignKey(Divisi, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='belum_terlaksana')
    jenis = models.CharField(max_length=20, choices=JENIS_CHOICES)
    untuk_semua = models.BooleanField(default=False)
    dibuat_oleh = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nama} ({self.jenis})"
    
class Gambar(models.Model):
    aktivitas = models.ForeignKey(Aktivitas, on_delete=models.CASCADE, related_name='gambar_list')
    gambar = models.ImageField(upload_to='gambar_kegiatan/')

    def __str__(self):
        return f"Gambar untuk {self.aktivitas.nama}"

