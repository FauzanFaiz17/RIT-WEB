from django.db import models

class Barang(models.Model):
    nama = models.CharField(max_length=255)
    kode = models.CharField(max_length=100, unique=True)
    jumlah = models.IntegerField()
    lokasi = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Peminjaman(models.Model):
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    peminjam = models.CharField(max_length=255)
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.peminjam} - {self.barang.nama}"
