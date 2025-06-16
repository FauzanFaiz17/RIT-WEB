from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class User(AbstractUser):
        PRODI_CHOICES = [
                ('-', 'Belum Diisi'),
        ("TI", "Teknologi Informasi"),
        ("RPL", "Rekayasa Perangkat Lunak"),
        ("RSK", "Rekayasa Sistem Komputer"),
        ("ILKOM", "Ilmu Komunikasi"),
    ]
        JABATAN_CHOICES = [
        ('ketua', 'Ketua'),
        ('sekretaris', 'Sekretaris'),
        ('bendahara', 'Bendahara'),
        ('humas', 'Humas'),
        ('anggota', 'Anggota'),
        ('Ketua Divisi', 'Ketua Divisi'),
        ('Ketua Komunitas', 'Ketua Komunitas'),
    ]
        no_hp = models.CharField(max_length=15, blank=True, default="")
        tanggal_lahir = models.DateField(null=True, blank=True)
        npm = models.CharField(max_length=15, unique=True, blank=True, null=True)
        prodi = models.CharField(max_length=50,choices=PRODI_CHOICES,blank=True,default="-")
        semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(14)],blank=True,null=True,default=1,)
        jabatan = models.CharField(max_length=20, choices=JABATAN_CHOICES, blank=True, null=True, default="Anggota")
        foto_profil = models.ImageField(upload_to="foto_profil/", blank=True, null=True)
        groups = models.ManyToManyField(
            'auth.Group',
            related_name='custom_user_groups',  # Unique related name for groups
            blank=True
        )
        user_permissions = models.ManyToManyField(
            'auth.Permission',
            related_name='custom_user_permissions',  # Unique related name for user_permissions
            blank=True
        )

def __str__(self):
    return f"{self.username} ({self.jabatan or 'Tanpa Jabatan'})"

class Komunitas(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField(null=True, blank=True)
    kepala = models.ForeignKey(User, related_name='kepala_komunitas', on_delete=models.SET_NULL, null=True, blank=True)
    anggota = models.ManyToManyField('User', related_name='anggota_komunitas')
    def __str__(self):
        return self.nama


class Divisi(models.Model):
    komunitas = models.ForeignKey(Komunitas, on_delete=models.CASCADE, related_name='divisi')
    nama = models.CharField(max_length=255)
    kepala = models.ForeignKey(User, related_name='kepala_divisi', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nama} ({self.komunitas.nama})"



class AnggotaDivisi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'divisi')

    def __str__(self):
        return f"{self.user.username} di {self.divisi.nama}"
