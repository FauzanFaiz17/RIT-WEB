from django.db import models

class Kegiatan(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    tanggal = models.DateField()

    def __str__(self):
        return self.nama

class GambarKegiatan(models.Model):
    kegiatan = models.ForeignKey(Kegiatan, related_name='gambar', on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to='gambar_kegiatan/')
    
    def __str__(self):
        return f"Gambar untuk {self.kegiatan.nama}"
