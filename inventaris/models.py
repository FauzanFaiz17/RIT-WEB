from django.db import models

class Barang(models.Model):
    nama_barang = models.CharField(max_length=255)
    sebelum = models.IntegerField()
    ditambah = models.IntegerField()
    digunakan = models.IntegerField()
    sisa = models.IntegerField()
    tanggal = models.DateField()
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class FotoBarang(models.Model):
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE, related_name='fotos')
    foto_barang = models.ImageField(upload_to="foto_barang/", blank=True, null=True)