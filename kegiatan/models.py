from django.db import models
from users.models import Komunitas

class Kegiatan(models.Model):
    komunitas = models.ForeignKey(Komunitas, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    tanggal = models.DateField()

    def __str__(self):
        return f"{self.nama} - {self.komunitas.nama}"
