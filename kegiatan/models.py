from django.db import models

class Kegiatan(models.Model):
    nama = models.CharField(max_length=100)
    tanggal = models.DateField()
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.nama
