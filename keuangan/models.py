from django.db import models

class Keuangan(models.Model):
    JENIS_CHOICES = (
        ('masuk', 'Pemasukan'),
        ('keluar', 'Pengeluaran'),
    )

    nama = models.CharField(max_length=100)
    tanggal = models.DateField()
    keterangan = models.TextField()
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)
    jenis = models.CharField(max_length=10, choices=JENIS_CHOICES)
    sisa = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.jenis.upper()} - {self.jumlah}"


class FotoKeuangan(models.Model):
    keuangan = models.ForeignKey(Keuangan, on_delete=models.CASCADE, related_name='fotos')
    foto_keuangan = models.ImageField(upload_to="foto_keuangan/", blank=True, null=True)