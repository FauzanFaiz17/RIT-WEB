from django.db import models
from django.contrib.auth.models import AbstractUser



class Blog(models.Model):
    nama= models.CharField(max_length=20)
    nomor= models.IntegerField(max_length=12)
    isi= models.CharField(max_length=512)

    

# Create your models here.

# class User(AbstractUser):
#     # Field tambahan
#     foto_profil = models.CharField(max_length=20, unique=True, null=True, blank=True,db_index=True)
#     tanggal_lahir = models.DateField(null=True, blank=True)
#     npm = models.CharField(max_length=20, unique=True, null=True, blank=True,db_index=True)
#     nomor_anggota = models.CharField(max_length=20, unique=True, null=True, blank=True,db_index=True)
#     nomor_telepon = models.CharField(max_length=15, null=True, blank=True)
#     alamat = models.CharField(null=True, blank=True)
#     # jurusan = models.ForeignKey(ProgramStudi, on_delete=models.SET_NULL, null=True, blank=True, related_name='users',db_index=True)

#     def __str__(self):
#         return self.username