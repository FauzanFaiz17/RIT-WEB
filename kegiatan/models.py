from django.db import models
from users.models import Komunitas,User

class Kegiatan(models.Model):
    STATUS_CHOICES = [
    ('terlaksana', 'Terlaksana'),
    ('tidak_terlaksana', 'Tidak Terlaksana'),
    ('belum_terlaksana', 'Belum Terlaksana'),
    ]
        
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    tanggal = models.DateField()
    jenis = models.CharField(max_length=255)
    ketua_pelaksana = models.ForeignKey(User, on_delete=models.CASCADE)
    komunitas = models.ForeignKey(Komunitas, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.nama} - {self.komunitas.nama}"

class FotoKegiatan(models.Model):
    kegiatan = models.ForeignKey(Kegiatan, on_delete=models.CASCADE, related_name='fotos')
    foto_kegiatan = models.ImageField(upload_to="foto_kegiatan/", blank=True, null=True)