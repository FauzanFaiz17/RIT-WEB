from django.db import models

class Transaksi(models.Model):
    KATEGORI_CHOICES = (
        ('masuk', 'Pemasukan'),
        ('keluar', 'Pengeluaran'),
    )

    tanggal = models.DateField()
    deskripsi = models.TextField()
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)
    kategori = models.CharField(max_length=10, choices=KATEGORI_CHOICES)

    def __str__(self):
        return f"{self.kategori.upper()} - {self.jumlah}"
