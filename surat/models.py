from django.db import models

class SuratMasuk(models.Model):
    nomor = models.CharField(max_length=100)
    pengirim = models.CharField(max_length=255)
    tanggal = models.DateField()
    perihal = models.CharField(max_length=255)
    file = models.FileField(upload_to='surat_masuk/')

    def __str__(self):
        return self.nomor

class SuratKeluar(models.Model):
    nomor = models.CharField(max_length=100)
    penerima = models.CharField(max_length=255)
    tanggal = models.DateField()
    perihal = models.CharField(max_length=255)
    file = models.FileField(upload_to='surat_keluar/')

    def __str__(self):
        return self.nomor
